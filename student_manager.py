import json

database = "students.json"

def load_file():
    try:
        with open(database, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_file():
    try:
        with open(database, "w") as file:
            json.dump(SanAg, file, indent=4)
    except Exception as e:
        print("Error Saving!", e)

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))

    SanAg.append({"name": name, "age": age})
    save_file()
    print(name, "added to the database")

def display_students():
    for i, student in enumerate(SanAg, start=1):
        print("Name:", student['name'], "| Age:", student['age'])


SanAg = load_file()

display_students()
print("Number of students:", len(SanAg))