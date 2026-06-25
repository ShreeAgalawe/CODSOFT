import json
import os

# File to store contacts persistently
CONTACTS_FILE = 'contacts.json'

def load_contacts():
    # Load contacts from the JSON file if it exists
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    # Save the current list of contacts to the JSON file
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()
    
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    save_contacts(contacts)
    print(f"\nSuccess: Contact '{name}' added successfully!")

def view_contacts(contacts):
    print("\n--- Contact List ---")
    if not contacts:
        print("Your contact book is currently empty.")
        return
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")
    print("--------------------")

def search_contact(contacts):
    print("\n--- Search Contact ---")
    query = input("Enter name or phone number to search: ").strip().lower()
    
    # List comprehension to find matches
    results = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    
    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"Name: {contact['name']} | Phone: {contact['phone']}")
            print(f"Email: {contact['email']} | Address: {contact['address']}\n")
    else:
        print("No contacts found matching your search.")

def update_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        index = int(input("\nEnter the number of the contact to update: ")) - 1
        if 0 <= index < len(contacts):
            print("\nLeave the field blank and press Enter to keep the current value.")
            contact = contacts[index]
            
            new_name = input(f"Enter new name ({contact['name']}): ").strip()
            new_phone = input(f"Enter new phone ({contact['phone']}): ").strip()
            new_email = input(f"Enter new email ({contact['email']}): ").strip()
            new_address = input(f"Enter new address ({contact['address']}): ").strip()
            
            # Update fields only if the user typed something new
            if new_name: contact['name'] = new_name
            if new_phone: contact['phone'] = new_phone
            if new_email: contact['email'] = new_email
            if new_address: contact['address'] = new_address
            
            save_contacts(contacts)
            print("\nSuccess: Contact updated!")
        else:
            print("Error: Invalid contact number.")
    except ValueError:
        print("Error: Please enter a valid number.")

def delete_contact(contacts):
    view_contacts(contacts)
    if not contacts:
        return
    try:
        index = int(input("\nEnter the number of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted = contacts.pop(index)
            save_contacts(contacts)
            print(f"\nSuccess: Contact '{deleted['name']}' deleted!")
        else:
            print("Error: Invalid contact number.")
    except ValueError:
        print("Error: Please enter a valid number.")

def main():
    contacts = load_contacts()
    while True:
        print("\n=== Secure Contact Book ===")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("\nExiting Contact Book. Goodbye!")
            break
        else:
            print("\nError: Invalid choice. Please select a number from 1 to 6.")

if __name__ == "__main__":
    main()