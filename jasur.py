# 2 -> find contact --done
# 3 -> delete contact --done
# 4 -> add to favour --processing

import json

with open('contacts.json', 'r') as file:
    json_data = file.read()

data = json.loads(json_data)
flag = True
name = str(input("Enter the name of the contact: "))
for i in data:
    if name == i["name"]:
        print("Contact found:")
        print(i["name"], i["phone"])
        flag = False
        break

if flag:
    print("Contact not found.")
else:
    editing = int(input("If you want to edit the contact, write 1. If you want to delete the contact, write 0: "))
    print("")
    if editing:
        pass
    else:
        data.remove(i)
        with open('contacts.json', 'w') as file:
            json.dump(data, file, indent=4)
        print("Contact deleted successfully.")
