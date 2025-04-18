import file_handler
from transaction import Transaction

from datetime import datetime

class BudgetTracker:
    def __init__(self):
        self.budget = file_handler.load_file()
        
    def save_file(self):
        file_handler.save_file(self.budget)
        
    def new_transaction(self, transaction):
        self.budget.append(transaction)
        self.save_file()
        
    def view_transactions(self, sort=0):
        print(f'{'Date':<15}{'Type':<15}{'Category':<20}{'Amount'}')
        print('-' * 60)
        
        match sort:
            case 1: # * Sort by amount
                sorted_transactions = sorted(self.budget, key=lambda t: t.amount, reverse=True)
            case 2: # * Sort by date
                sorted_transactions = sorted(self.budget, key=lambda t: datetime.strptime(t.date, "%m/%d/%Y"))
            case 3: # * Sort by category
                sorted_transactions = sorted(self.budget, key=lambda t: t.category)
            case 4: # * Sort by type
                sorted_transactions = sorted(self.budget, key=lambda t: t.types)
                    
        for t in sorted_transactions:
            print(f'{t.date:<15}{t.types:<15}{t.category:<20}{t.amount}')             
                    
        total = sum(t.amount if t.types == "Income" else -t.amount for t in self.budget)
                
        print('-' * 60)
        print(f'{' ':<50}{'Total: '}{total}')
        
    def view_summary(self):
        total_income = 0
        total_expenses = 0
        
        print(f'{'Total Income':<20}{'Total Expenses':<20}{'Net Balance'}')
        print('-' * 50)
        
        for t in self.budget:
            if t.types == "Income":
                total_income += t.amount
            else:
                total_expenses += t.amount
        
        net_balance = total_income - total_expenses
        
        print(f'{total_income:<20}{total_expenses:<20}{net_balance}')
        print('-' * 50)
        
    def monthly_breakdown(self):
        
        months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ]
        
        breakdown = []
        
        for i in range(1, 13):
            total = 0
            for t in self.budget:
                date = datetime.strptime(t.date, "%m/%d/%Y")
                if t.types == "Income" and date.month == i:
                    total += t.amount
                elif t.types == "Expenses" and date.month == i:
                    total -= t.amount
            breakdown.append(total)
                    
        for i, month in enumerate(months, start=0):  
            print(f"{month}: {breakdown[i]}")