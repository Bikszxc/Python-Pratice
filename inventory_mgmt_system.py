import time
import os

class InventorySystem:
    __inventory = {}

    def __init__(self):
        pass

    @classmethod
    def add_item(self, name, qty):
        if name not in self.__inventory and qty > 0:
            self.__inventory[name] = qty
        else:
            raise ValueError
    @classmethod
    def remove_item(self, name):
        if name in self.__inventory:
            del self.__inventory[name]
        else:
            raise ValueError

    @classmethod
    def update_qty(self, name, qty):
        if name in self.__inventory and qty > 0:
            self.__inventory[name] = qty
        else:
            raise ValueError

    @classmethod
    def check_inventory(self):
        return self.__inventory
        
def main_menu():
    while True:
        print("-" * 15, "IMS", "-" * 15)
        print("1. Add Item\n2. Remove Item\n3. Update item quantity\n4. Display inventory\n5. Exit")

        choice = int(input("Enter your choice: "))
        os.system('cls')
        match choice:
            case 1:
                while True:
                    try:
                        item_name = input("Enter item name to add: ")
                        qty = int(input("Enter quantity: "))
                        InventorySystem.add_item(item_name, qty)
                        print("Added", qty, item_name, "to the inventory!")
                        time.sleep(2)
                        os.system('cls')
                        break
                    except ValueError:
                        print("Item already exists!")
            case 2:
                while True:
                    try:
                        item_name = input("Enter item name to remove: ")
                        InventorySystem.remove_item(item_name)
                        print("Removed", item_name, "from the inventory!")
                        time.sleep(2)
                        os.system('cls')
                        break
                    except ValueError:
                        print("Item does not exist!")
            case 3:
                while True:
                    try:
                        item_name = input("Enter item name to update qty: ")
                        qty = int(input("Enter quantity: "))
                        print("Updated quantity of", item_name, "to", qty)
                        InventorySystem.update_qty(item_name, qty)
                        time.sleep(2)
                        os.system('cls')
                        break
                    except ValueError:
                        print("Item does not exist!")
            case 4:
                print("Inventory")
                for item in InventorySystem.check_inventory():
                    print(item, "-", InventorySystem.check_inventory().get(item))
                
                done = input("Press enter when done... ").strip()
                if done == " ":
                    os.system('cls')
                    break
            case 5:
                main_menu()

main_menu()