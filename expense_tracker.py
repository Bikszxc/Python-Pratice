class Expense:
    def __str__(self, amount, category, date):
        return "-" , amount, " - ", category, " - ", f"({date})"
        

class ExpenseTracker:
    def __init__(self, expenses=[]):
        self.expenses = expenses

    def add_expense(self, amount, category, date):
        self.expenses.append({"Amount": amount, "Category": category, "Date": date})

    def view_expenses(self):
        for expense in self.expenses:
            for key, value in expense.items():
                Expense()
                

tracker = ExpenseTracker()

tracker.add_expense(100, "Tite", "2024-10-15")
tracker.add_expense(150, "Meow", "2024-11-15")
tracker.view_expenses()
