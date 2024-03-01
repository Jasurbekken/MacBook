# 2 -> find contact --done
# 3 -> delete contact --done
# 4 -> add to favour --done

import json
import os

def load_contacts(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            json_data = file.read()
        if json_data:
            return json.loads(json_data)
        else:
            return []
    else:
        return []

def save_contacts(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

contacts = load_contacts('contacts.json')

name = input("Enter the name of the contact: ")

found_contacts = []
for contact in contacts:
    if name.lower() == contact["name"].lower():
        found_contacts.append(contact)

if not found_contacts:
    print("Contact not found.")
else:
    print("Contacts found:")
    for idx, contact in enumerate(found_contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")
    
    choice = input("Enter the number of the contact you want to edit/delete, or '0' to cancel: ")
    
    if choice.isdigit():
        choice = int(choice)
        if 0 < choice <= len(found_contacts):
            selected_contact = found_contacts[choice - 1]
            print("Selected Contact:", selected_contact)
            action = input("Enter '1' to edit the contact, '0' to delete the contact, 'favourite' to add to favourites, or 'cancel' to cancel: ")
            
            if action.lower() == '1':
                # Editing code goes here
                pass
            elif action.lower() == '0':
                contacts.remove(selected_contact)
                save_contacts('contacts.json', contacts)
                print("Contact deleted successfully.")
            elif action.lower() == 'favourite':
                favourites = load_contacts('favourites.json')
                favourites.append(selected_contact)
                save_contacts('favourites.json', favourites)
                print("Contact added to favorites successfully.")
            else:
                print("Invalid action. No changes made.")
        else:
            print("Invalid choice. No changes made.")
    else:
        print("Invalid choice. No changes made.")

