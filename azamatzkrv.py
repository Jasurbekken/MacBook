# 5 -> edit contact
# 6 -> trash & recovery
# 7 -> set password & reset password

# def edit_contact():
#     with open("/txt_files/")
from json import dumps,loads
from os import system
def editor(Key,dict_of_number):
    with open("contacts.json",'r') as json_file:
        a = json_file.read()
        python_file = loads(a)
    if Key == 1:
        phone = dict_of_number[Key-1]["phone"]
        dict_of_number.clear()
        name = input("new name: ")
        dict_of_number[Key-1]["name"] = name
        dict_of_number[Key-1]["phone"] = phone
    elif Key == 2:
        name = dict_of_number[Key-1]["name"]
        dict_of_number.clear()
        phone = input("new phoone number: ")
        dict_of_number[Key-1]["name"] = name
        dict_of_number[Key-1]["phone"] = phone
    elif Key == 3:
        dict_of_number.clear()
        name = input("new name: ")
        name = input("new phone number: ")
        dict_of_number[Key-1]["name"] = name
        dict_of_number[Key-1]["phone"] = phone


def edit_contact():
    with open("contacts.json",'r') as json_file:
        a = json_file.read()
        python_file = loads(a)
    for i in range(len(python_file)):
        print(i+1,": name: ",python_file[i]["name"]," phone number: ",python_file[i]["phone"])
    
    flag = False
    while flag != True:
        try:
            a = int(input(f"choose from 1 to {len(python_file)}: "))
            if a <= 0 or a >= len(python_file):
                system("clear")
                print("you do not have this type of menue")
                for i in range(len(python_file)):
                    print(i+1,": name: ",python_file[i]["name"]," phone number: ",python_file[i]["phone"])
            else:
                flag = True
        except ValueError:
            system("clear")
            print("please enter only real number")
            for i in range(len(python_file)):
                print(i+1,": name: ",python_file[i]["name"]," phone number: ",python_file[i]["phone"])
    flag = False
    while flag != True:
        try:
            a = int(input("which one will you change 1 -> Name/ 2 - > Phone number / 3 -> Both: "))
            if a > 3 or a <= 0:
                system("clear")
                print("you can not do that ")
            else:
                editor(a,python_file)
                flag = True
        except ValueError:
            system("clear")
            print("you can not do that ")
edit_contact()