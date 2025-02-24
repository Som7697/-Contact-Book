
contacts = {}

def add_contact():
    """Add a new contact"""
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    address = input("Enter address: ").strip()
    
    if name in contacts:
        print("Contact already exists!")
    else:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print("Contact added successfully!")

def view_contacts():
    """View all contacts"""
    if not contacts:
        print("No contacts found!")
    else:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}")

def search_contact():
    """Search for a contact"""
    query = input("Enter name or phone number to search: ").strip()
    found = False
    for name, details in contacts.items():
        if query == name or query == details["Phone"]:
            print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}")
            found = True
            break
    if not found:
        print("Contact not found!")

def update_contact():
    """Update an existing contact"""
    name = input("Enter the name of the contact to update: ").strip()
    if name in contacts:
        phone = input("Enter new phone number: ").strip()
        email = input("Enter new email: ").strip()
        address = input("Enter new address: ").strip()
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact():
    """Delete a contact"""
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def menu():
    """Display the menu and handle user input"""
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

menu()