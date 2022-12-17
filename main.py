from Function import *
from data import *


helper = input("Do you need a list of available features? (Y/N): ")
if helper.lower() == "y":
    print("The list of commands: \n", HELP)

while True:
    command = input("Enter command: ").lower()
    if command == "p":
        people()
    elif command == "s":
        shelf()
    elif command == "l":
        list_doc()
    elif command == "a":
        add()
    elif command == "d":
        delete()
    elif command == "as":
        add_shelf()
    elif command == "m":
        print("Available shelves: \n")
        for key in directories.keys():
            print(key.capitalize())
        print()
        move()
    elif command == "h":
        print("The list of commands: \n", HELP)
    elif command == "exit":
        exit()
    else:
        print("There is no such command in the list")
