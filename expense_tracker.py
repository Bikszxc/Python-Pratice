import json
import os
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class ExpenseTracker:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    def save_expenses(self):
        try:
            with open(self.filename, "w") as file:
                json.dump(self.expenses, file, indent=4)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
        
    def add_expenses(self, desc, category, amount, date):
        self.new_expense = {"description": desc, "category": category, "amount": amount, "date": date}
        self.expenses.append(self.new_expense)
        self.save_expenses()
        
    def view_expenses(self):
        print("-" * 18, "List of All Expenses", "-" * 18)
        print(f"{'No.':<5}{'Description':<15}{'Category':<15}{'Amount':<15}{'Date'}")
        print("-" * 58)
        for i, expense in enumerate(self.expenses, start=1):
            amount = f"{expense['amount']:,.2f}"
            print(f"{str(i):<5}{expense['description']:<15}{expense['category']:<15}{amount:<15}{expense['date']}")
        print("-" * 58)

    def view_total(self):
        print("-" * 15, "Expenses Breakdown", "-" * 15)
        print(f"{'Food':<15}{'Needs':<15}{'Others':<15}{'Total':<15}")
        print("-" * 50)

        food = sum(expense["amount"] for expense in self.expenses if expense["category"].lower() == "food".lower())
        needs = sum(expense["amount"] for expense in self.expenses if expense["category"].lower() == "needs".lower())
        others = sum(expense["amount"] for expense in self.expenses if expense["category"].lower() == "others".lower())
        total = food + needs + others

        print(f"{food:<15,.2f}{needs:<15,.2f}{others:<15,.2f}{total:<15,.2f}")

        print("-" * 50)

ExpTrack = ExpenseTracker()

while True:
    print("-" * 15, "Expense Tracker", "-" * 15)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Breakdown")
    print("4. Exit")
    try:
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                clear_screen()
                print("Expense Tracker - Add Expense")
                while True:
                    try:
                        desc = input("Enter a description: ")
                        if desc == "".strip():
                            raise ValueError("Description cannot be blank")
                        else:
                            break
                    except ValueError:
                        print("Invalid input!")

                while True:
                    print(f"{"1. Food":<10}{"2. Needs":<10}{"3. Others":<10}")
                    try:
                        category = int(input("Select a category: "))
                        match category:
                            case 1:
                                category = "Food"
                                break
                            case 2:
                                category = "Needs"
                                break
                            case 3:
                                category = "Others"
                                break
                            case _:
                                print("Invalid Choice!")
                    except ValueError:
                        print("Invalid input!")

                while True:
                    try:
                        amount = float(input("Enter the amount: "))
                        if amount < 1:
                            print("Amount cannot be below than 1")
                        else:
                            break
                    except ValueError:
                        print("Invalid Input!")
                    
                while True:
                    date = input("Enter date of spending (YYYY-MM-DD): ").strip()
                    try:
                        datetime.strptime(date, "%Y-%m-%d")
                        break
                    except ValueError:
                        print("Invalid date format! (YYYY-MM-DD)")
                    
                ExpTrack.add_expenses(desc, category, amount, date)
            case 2:
                clear_screen()
                ExpTrack.view_expenses()
                input("Press enter to go back to main menu...")
            case 3:
                clear_screen()
                ExpTrack.view_total()
                input("Press enter to go back to main menu...")
            case 4:
                clear_screen()
                print("Thanks for using our expense tracker!")
                exit()
            case _:
                print("Invalid choice!")

        clear_screen()

    except ValueError:
        print("Invalid Input!")