documents = [

]

directories = {

}

HELP = """
    p - the command to search for the owner by document number,
    s - the command shows the shelf on which the document is stored,
    l - the command displays all the documents that are in the list,
    a - the command adds information about the new document and its owner, and also adds the document to the desired shelf,
    d - the command removes all information about the document, the owner from the list and removes the document from the shelf,
    as - the command adds a new empty shelf,
    m - the command moves the document to another required shelf shelf
    h - the command will open the list of available commands again,
    exit - the command will terminate the program.
"""


def people():
    """ This function helps to find a person with his document"""

    number_doc = input("Enter document number: ")

    for i, el in enumerate(documents):
        docs_arr = list(documents[i].items())
        number = docs_arr[1][1]
        if number == number_doc in docs_arr[1][1]:
            print(f"The owner of the document with the number {number_doc}: {docs_arr[2][1]}")
            break
    else:
        print("Document with this number does not exist!")
    print()


def shelf():
    """This function shows name of directory of document"""

    number_doc = input("Enter document number: ")

    for i, el in enumerate(directories):
        list(directories.items())
        if number_doc in list(directories.items())[i][1]:
            print(f"Document with number {number_doc} is on the shelf {list(directories.items())[i][0]}")
            break
    else:
        print("Document with this number does not exist!")
    print()


def list_doc():
    """This function shows all list of documents"""

    for docs in documents:
        for i, el in enumerate(directories):
            list(directories.items())
            if docs['number'] in list(directories.items())[i][1]:
                print(f"Document type: {docs['type']}, document number: {docs['number']}, owner name: {docs['name']},"
                      f" document is on the shelf:  {list(directories.items())[i][0]}")
    print()


def add():
    """This function adds new information to documents and directories"""

    name = input("Enter owner name: ")
    type_doc = input("Enter document type: ")
    number_doc = input("Enter document number: ")

    dict_new = {"type": type_doc.lower(), "number": number_doc, "name": name}
    documents.append(dict_new)
    if type_doc in directories.keys():
        directories[type_doc.lower()].append(number_doc)
    else:
        directories[type_doc.lower()] = [number_doc]
    print("Done!")
    print()


def delete():
    """This function removes all information from documents and directories"""

    number_doc = input("Enter document number: ")

    for i, el in enumerate(documents):
        docs_arr = list(documents[i].items())
        if number_doc == docs_arr[1][1]:
            documents.remove(documents[i])
            print(f"All information about document number {number_doc} has been removed.")
            break
    else:
        print("Document with this number does not exist!")
        print()
    for key, value in directories.items():
        if number_doc in value:
            directories[key].remove(number_doc)
            if directories[key] is None:
                directories[key] = []
                break
            else:
                pass


def add_shelf():
    """This function adds new shelf to directories with empty array"""

    type_doc = input("Enter document type: ")

    if type_doc not in directories:
        directories[type_doc.lower()] = []
        print(f"Shelf named {type_doc} added!")
    else:
        print("The shelf with the same name already exists.")
    print()


def move():
    """This function move document from previous directory to new (main func)"""
    type_doc = input("Enter a name for the new shelf: ").lower()
    type_doc_old = input("Enter the name of the current shelf: ").lower()
    number_doc = input("Enter document number: ")

    if type_doc in directories.keys():
        if type_doc_old in directories.keys():
            for value in directories.values():
                if number_doc in value:
                    move_body(type_doc, type_doc_old, number_doc)
                    break
            else:
                print("Document with this number does not exist!")
        else:
            print("Shelf with this name does not exist!")
    else:
        print("Shelf with this name does not exist!")

    print()


def move_body(type_doc, type_doc_old, number_doc):
    """This function move document from previous directory to new (body func)"""

    if number_doc in directories[type_doc_old]:
        directories[type_doc_old].remove(number_doc)
        if directories[type_doc_old] is None:
            directories[type_doc_old] = []
        else:
            pass
        for key in directories.keys():
            if key == type_doc:
                directories[key].append(number_doc)
    else:
        print(f"Document with number {number_doc} is not on the shelf {type_doc_old}")

    print()


helper = input("Do you need a list of available features? (Y/N): ")
if helper.lower() == "y":
    print(HELP)

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
        print(HELP)
    elif command == "exit":
        exit()
    else:
        print("There is no such command in the list")