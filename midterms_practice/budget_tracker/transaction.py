class Transaction:
    def __init__(self, amount, types, category, date):
        self.amount = amount
        self.types = types
        self.category = category
        self.date = date
    
    def to_dict(self):
        return{
            "amount": self.amount,
            "types": self.types,
            "category": self.category,
            "date": self.date
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            amount=data["amount"],
            types=data["types"],
            category=data["category"],
            date=data["date"]
        )
        