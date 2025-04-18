from budget_tracker import BudgetTracker
from transaction import Transaction

bt = BudgetTracker()

def main():
    
    choices = ["1. Add Transaction", "2. View Transactions", "3. Summary of All Transactions", "4. Monthly Breakdown", "5. Exit"]
    
    print('-' * 10, 'Budget Tracker', '-' * 10)
    for item in choices:
        print(item)

if __name__ == '__main__':
    main()
