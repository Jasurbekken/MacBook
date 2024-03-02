# Introduction
# Menues
# 0 -> Create accounts
# 1 -> Create contact

from time import sleep
from os import system
from json import dumps, loads

name = None
phone = None
flag = 0

for i in range(5,-1,-1):
    print("Hello welcome my program")
    print(i)
    sleep(1)
    system("cls")
    
for i in range(5,-1,-1):
    print("Program will start with in [5] seconds")
    print(i)
    sleep(1)
    system("cls")
    
print("WELCOME")
sleep(1)
system("cls")
name = input("Enter name: ")
print("Your phone numbers must start with these numbers\n+99890\n+99891\n+99893\n+99894\n+99895\n+99897\n+99899\n+99888\n+99920")

while flag != True:
    try:
        phoneNumber = input("Please enter your number: ")
        if(card[:5] == "+99890" or card[:5] == "+99891" or card[:5] == "+99893" or card[:5] == "+99894" or card[:5] == "+99895" or card[:5] == "+99897" or card[:5] == "+99899" or card[:5] == "+99888" or card[:5] == "+99820") and len(card) == 13:
            break
        else:
            system("cls")
            print("Sorry our company support this numbers !!!\n+99890\n+99891\n+99893\n+99894\n+99895\n+99897\n+99899\n+99888\n+99920")
    except ValueError:
        system("cls")
        print("Invalid number ! Please try again")
        
with open("contacts.json", "r") as read_from_json:
    data = loads(read_from_json.read())

dict1 = {}
dict1["name"] == 
data.append(dict1)

with open("contacts.json", "w") as write_to_json:
    k = dumps(data, indent=4)
    write_to_json.write(k)
