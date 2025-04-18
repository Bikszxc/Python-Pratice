import json, os, csv
from datetime import datetime, date

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Project:
    def __init__(self, name, client, deadline, status="Ongoing"):
        self.name = name
        self.client = client
        # If deadline is a string, convert it to a datetime object
        if isinstance(deadline, str):
            self.deadline = datetime.strptime(deadline, "%m/%d/%Y")
        else:
            self.deadline = deadline
        self.status = status

    def get_deadline(self):
        # Format the deadline as a string if it's a datetime object
        return self.deadline.strftime("%m/%d/%Y") if isinstance(self.deadline, datetime) else self.deadline

    def to_dict(self):
        # Save the deadline in string format for JSON compatibility
        return {
            "name": self.name,
            "client": self.client,
            "deadline": self.deadline.strftime("%m/%d/%Y") if isinstance(self.deadline, datetime) else self.deadline,
            "status": self.status
        }
    
    @staticmethod
    def from_dict(data):
        """
        Converts a dictionary (typically from JSON) into a Project instance.
        Handles the conversion of 'deadline' from a string to a datetime object.
        """
        # If 'deadline' is a string, convert it to a datetime object
        if isinstance(data['deadline'], str):
            data['deadline'] = datetime.strptime(data['deadline'], "%m/%d/%Y")
        
        # Return an instance of the Project class using the data
        return Project(
            name=data["name"],
            client=data["client"],
            deadline=data["deadline"],  # Now a datetime object
            status=data["status"]
        )

class ProjectTracker:
    def __init__(self, filename="projects.json"):
        self.filename = filename
        self.projects = self.load_file()

    def load_file(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return [Project.from_dict(p) for p in data]
        except (FileNotFoundError, json.JSONDecodeError):
            print("There's an error with your save file.")
            return []
        
    def save_file(self):
        try:
            with open(self.filename, "w") as file:
                json.dump([project.to_dict() for project in self.projects], file, indent=4)
        except Exception as e:
            print(f"Error! {e}")

    def export_to_csv(self, csv_filename="projects.csv"):
        try:
            with open(csv_filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Project Name", "Client", "Deadline", "Status"])

                for project in self.projects:
                    writer.writerow([
                        project.name,
                        project.client,
                        project.get_deadline(),
                        project.status
                    ])
                print(f"Projects successfully exported to {csv_filename}")
        except Exception as e:
            print(f"Error! {e}")

    def display_projects(self):
        ongoing = sorted([p for p in self.projects if p.status == "Ongoing"], 
                         key=lambda p: p.deadline)
        
        completed = [p for p in self.projects if p.status == "Completed"]

        if not ongoing:
            sort = completed
        else:
            sort = ongoing + completed

        spacing = max(len(proj.name) for proj in self.projects) + 5

        print(f"{'No':<5}{'Project Name':<{spacing}}{'Client':<25}{'Deadline':<15}{'Status'}")
        print("-" * (55 + spacing))
        for i, proj in enumerate(sort, start=1):
            print(f"{i:<5}{proj.name:<{spacing}}{proj.client:<25}{proj.get_deadline():<15}{proj.status}")
        
    def search(self, query):
        query = query.strip().lower()
        client_results = [p for p in self.projects if query in p.client.lower()]
        name_results = [p for p in self.projects if query in p.name.lower()]

        results = client_results + name_results
        
        if results:
            spacing = max(len(proj.name) for proj in results) if max(len(proj.name) for proj in results) > 20 else 20
            print(f"{'No':<5}{'Project Name':<{spacing}}{'Client':<20}{'Deadline':<15}{'Status'}")
            print("-" * 70)
            for i, proj in enumerate(results, start=1):
                print(f"{i:<5}{proj.name:<{spacing}}{proj.client:<20}{proj.get_deadline():<15}{proj.status}")
        else:
            print("No client found with your search.")
            
    def archive_completed(self, filename="project_archives.json"):

        archive = []

        for p in self.projects[:]:
            if p.status == "Completed":
                archive.append(p)
                self.projects.remove(p)

        try:
            with open(filename, "w") as file:
                json.dump([p.to_dict() for p in archive], file, indent=4)
                self.save_file()
                return f"Successfully archived all completed projects!"
        except Exception as e:
            print(f"Error Saving! {e}")

    def add_project(self, project):
        self.projects.append(project)
        self.save_file()

    def edit_project(self, choice, field, new_value):
        ongoing = sorted([p for p in self.projects if p.status == "Ongoing"], key=lambda p: p.deadline)
        completed = [p for p in self.projects if p.status == "Completed"]
        displayed_projects = ongoing + completed

        choice = choice - 1

        if 0 <= choice < len(displayed_projects):
            selected_project = displayed_projects[choice]

            if field == "name":
                selected_project.name = new_value
            elif field == "client":
                selected_project.client = new_value
            elif field == "deadline":
                try:
                    selected_project.deadline = datetime.strptime(new_value, "%m/%d/%Y")
                except ValueError:
                    return "Invalid date format. Use MM/DD/YYYY."
            else:
                return "Invalid field."

            self.save_file()
            return f"Successfully updated {field} of project."
        else:
            return "Invalid project choice."

    def change_status(self, choice):

        ongoing = sorted([p for p in self.projects if p.status == "Ongoing"], 
                         key=lambda p: p.deadline)
        
        completed = [p for p in self.projects if p.status == "Completed"]
        displayed_projects = ongoing + completed

        choice = choice - 1

        if 0 <= choice < len(self.projects):
            selected_project = displayed_projects[choice]
            
            for p in self.projects:
                if p.name == selected_project.name and p.client == selected_project.client:
                    p.status = "Completed" if p.status == "Ongoing" else "Ongoing"
                    break

            self.save_file()

            return f"Changed the status of {selected_project.name} from {selected_project.client}."
        else:
            raise ValueError("Invalid Project Choice!")
        
    def project_summary(self):

        today = datetime.today()
        current_year, current_week, _ = today.isocalendar()

        ongoing = [p for p in self.projects if p.status == "Ongoing"]
        completed = [p for p in self.projects if p.status == "Completed"]
        due_soon = [p for p in self.projects if p.status == "Ongoing" and p.deadline.isocalendar()[1] == current_week and p.deadline.isocalendar()[0] == current_year]

        print("Ongoing:", len(ongoing))
        print("Completed:", len(completed))
        print("Due Soon:", len(due_soon))

pm = ProjectTracker()

def main():
    def display_menu():
        width = 45
        header = "Project Tracker"
        options = [
            "Add Project",
            "Change Project Status",
            "Edit Project",
            "View All Projects",
            "View Project Summary",
            "Search Project",
            "Export to CSV",
            "Archive Completed",
            "Exit"
        ]

        print("-" * width)
        print(f"{header:^{width}}")
        print("-" * width)
        if notification:
            print(f"\n{notification}\n")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        print()

    def menu_addproj():
        project_name = input("Enter project name: ")
        client_name = input("Enter client name: ")

        while True:
            deadline = input("Enter deadline (MM/DD/YYYY): ")
            try:
                deadline = datetime.strptime(deadline, "%m/%d/%Y")
                break
            except ValueError:
                print("Invalid Date Format!")

        new_project = Project(project_name, client_name, deadline)
        pm.add_project(new_project)

        clear_screen()
        return f"{project_name} for {client_name} added successfully!"

    def menu_changestatus():
        pm.display_projects()

        while True:
            try:
                choice = int(input("Enter the project number to change its status: "))
                notif = pm.change_status(choice)
                break
            except ValueError:
                print("Invalid Input!")

        clear_screen()
        return notif

    def menu_editproj():
        pm.display_projects()

        while True:
            try:
                choice = int(input("Enter the project number to edit: "))
                print("1. Project Name | 2. Client Name | 3. Deadline")
                field = int(input("Enter the number of field to edit: "))
                new_value = input("Enter the changes: ")
                break
            except ValueError:
                print("Invalid input!")

        field_dict = {1: "name", 2: "client", 3: "deadline"}
        field = field_dict.get(field)

        notification = pm.edit_project(choice, field, new_value)
        return notification

    def menu_viewproj():
        pm.display_projects()
        input("\nPress any key to continue...")
        clear_screen()

    def menu_searchproj():
        search = input("Enter your search (Project Name or Client Name): ")
        pm.search(search)
        input("\nPress any key to continue...")
        clear_screen()

    def menu_exportcsv():
        filename = f"{date.today()} - Project Tracker.csv"
        pm.export_to_csv(filename)
        clear_screen()
        return f"Projects successfully exported to {filename}"

    notification = ""
    while True:
        display_menu()

        try:
            choice = int(input("Enter choice >> "))

            match choice:
                case 1:
                    clear_screen()
                    notification = menu_addproj()
                case 2:
                    clear_screen()
                    notification = menu_changestatus()
                case 3:
                    clear_screen()
                    notification = menu_editproj()
                case 4:
                    clear_screen()
                    menu_viewproj()
                    notification = ""
                case 5:
                    clear_screen()
                    pm.project_summary()
                    notification = ""
                    input("Press any key to continue...")
                    clear_screen()
                case 6:
                    clear_screen()
                    menu_searchproj()
                    notification = ""
                case 7:
                    notification = menu_exportcsv()
                case 8:
                    notification = pm.archive_completed()
                    clear_screen()
                case 9:
                    exit()
                case _:
                    print("Invalid choice.")
        except ValueError:
            print("Invalid input!")

if __name__ == "__main__":
    main()