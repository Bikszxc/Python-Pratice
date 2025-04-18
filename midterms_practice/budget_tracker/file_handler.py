import json
from transaction import Transaction

filename = "midterms_practice/budget_tracker/data/transactions.json"

def load_file():
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return [Transaction.from_dict(t) for t in data]
    except (FileNotFoundError, json.JSONDecodeError):
        print("There's an error with the save file")
        return []
    
def save_file(data):
    try:
        with open(filename, "w") as file:
            json.dump([t.to_dict() for t in data], file, indent=4)
    except Exception as e:
        print(f"Error Saving! {e}")