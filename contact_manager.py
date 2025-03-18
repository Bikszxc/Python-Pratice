import json
import re  # For email validation

# Load contacts from file
def load_file():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save contacts to file
def save_file():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

# Email validation function
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

# Add a contact with improved error handling
def add_contact():
    while True:
        contact_name = input("Enter contact name: ").strip()
        if not contact_name:
            print("Name cannot be empty!")
        elif any(contact["name"].lower() == contact_name.lower() for contact in contacts):
            print("A contact with that name already exists!")
        else:
            break

    while True:
        try:
            phone_number = input("Enter phone number: ").strip()
            if not phone_number.isdigit():
                raise ValueError("Phone number should contain digits only.")
            if any(contact["phone"] == phone_number for contact in contacts):
                print("A contact with that number already exists!")
            else:
                break
        except ValueError as e:
            print(e)

    while True:
        email_address = input("Enter email address: ").strip()
        if not email_address:
            print("Email cannot be empty!")
        elif not is_valid_email(email_address):
            print("Invalid email format! Example: example@domain.com")
        elif any(contact["email"].lower() == email_address.lower() for contact in contacts):
            print("A contact with that email address already exists!")
        else:
            break

    contacts.append({"name": contact_name, "phone": phone_number, "email": email_address})
    save_file()
    print("Contact added successfully!")

# View all contacts
def view_contacts():
    print(f"{'No.':<5}{'Name':<15}{'Phone':<15}{'Email'}")
    print("-" * 50)
    for i, contact in enumerate(contacts, start=1):
        print(f"{str(i):<5}{contact['name']:<15}{contact['phone']:<15}{contact['email']}")

# Delete a contact
def delete_contact():
    view_contacts()
    try:
        delete = int(input("Enter the number to delete: "))
        if delete < 1 or delete > len(contacts):
            print("Out of range!")
            return
        
        confirmation = input(f"Are you sure you want to delete '{contacts[delete - 1]['name']}'? (y/n): ").strip().lower()
        if confirmation == 'y':
            contacts.pop(delete - 1)
            save_file()
            print("Contact deleted successfully!")
        else:
            print("Deletion cancelled.")
    except ValueError:
        print("Invalid input!")

# Search for a contact
def search_contact():
    search_name = input("Enter the name of the contact to search: ").strip()
    found_contact = next((contact for contact in contacts if contact["name"].lower() == search_name.lower()), None)
    
    if found_contact:
        print("\nContact found:")
        print(f"{'Name:':<10}{found_contact['name']}")
        print(f"{'Phone:':<10}{found_contact['phone']}")
        print(f"{'Email:':<10}{found_contact['email']}")
    else:
        print("Contact not found.")

# Main program loop
contacts = load_file()

while True:
    print("-" * 15, "Contact Manager", "-" * 15)
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. View All Contacts")
    print("5. Exit")
    
    try:
        choice = int(input("Enter choice: "))
        match choice:
            case 1: add_contact()
            case 2: delete_contact()
            case 3: search_contact()
            case 4: view_contacts()
            case 5: 
                print("Goodbye!")
                break
            case _: print("Invalid choice!")
    except ValueError:
        print("Invalid input!")