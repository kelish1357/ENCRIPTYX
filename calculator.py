contactbook = {}

def add_contact():
    print("\nAdd Contact")
    print("------------")
    name = input("Enter name: ")
    phonenumber = input("Enter phone number: ")
    contactbook[name] = phonenumber
    print("Contact added successfully!")

def view_contacts():
    print("\nView Contacts")
    print("------------")
    if not contactbook:
        print("No contacts found!")
    else:
        print("Name\tPhone Number")
        for name, phonenumber in contactbook.items():
            print(f"{name}\t{phonenumber}")

def search_contact():
    print("\nSearch Contact")
    print("------------")
    search_term = input("Enter name to search: ")
    if search_term in contactbook:
        print(f"Name: {search_term}, Phone Number: {contactbook[search_term]}")
    else:
        print("Contact not found!")

def update_contact():
    print("\nUpdate Contact")
    print("------------")
    search_term = input("Enter name to update: ")
    if search_term in contactbook:
        phone_number = input("Enter new phone number: ")
        contactbook[search_term] = phone_number
        print("Contact updated successfully!")
    else:
        print("Contact not found!")

def delete_contact():
    print("\nDelete Contact")
    print("------------")
    search_term = input("Enter name to delete: ")
    if search_term in contactbook:
        del contactbook[search_term]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")