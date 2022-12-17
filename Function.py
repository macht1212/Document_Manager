from data import *
from main import *
import tkinter


def people(event):
    """ This function helps to find a person with his document"""

    number_doc = ppl.get()

    for docs in documents:
        docs_arr = list(docs.items())
        number = docs_arr[1][1]
        if number == number_doc in docs_arr[1][1]:
            print(f"The owner of the document with the number {number_doc}: {docs_arr[2][1]}")
            break
    else:
        print("Document with this number does not exist!")
    print('\n')


# def shelf():
#     """This function shows name of directory of document"""

#     number_doc = input("Enter document number: ")

#     for i, el in enumerate(directories):
#         list(directories.items())
#         if number_doc in list(directories.items())[i][1]:
#             print(f"Document with number {number_doc} is on the shelf {list(directories.items())[i][0]}")
#             break
#     else:
#         print("Document with this number does not exist!")
#     print('\n')


def list_doc():
    """This function shows all list of documents"""

    if documents == []:
        print('Data is empty! Create somthing with command "a".')
    else:
        for docs in documents:
            print(f"Document type: {docs['type']}, document number: {docs['number']}, owner name: {docs['name']}")
    print('\n')


def add():
    """This function adds new information to documents and directories"""

    # name = 
    # type_doc = 
    # number_doc = 

    dict_new = {"type": type_doc.lower(), "number": number_doc, "name": name}
    documents.append(dict_new)
    print("Done!")
    print('\n')


def delete():
    """This function removes all information from documents and directories"""

    # number_doc = 

    for doc in documents:
        docs_arr = list(doc.items())
        if number_doc == docs_arr[1][1]:
            documents.remove(doc)
            print(f"All information about document number {number_doc} has been removed.")
            break
    else:
        print("Document with this number does not exist!")
        print('\n')
    # for key, value in directories.items():
    #     if number_doc in value:
    #         directories[key].remove(number_doc)
    #         if directories[key] is None:
    #             directories[key] = []
    #             break
    #         else:
    #             pass


# def add_shelf():
#     """This function adds new shelf to directories with empty array"""

#     type_doc = input("Enter document type: ")

#     if type_doc not in directories:
#         directories[type_doc.lower()] = []
#         print(f"Shelf named {type_doc} added!")
#     else:
#         print("The shelf with the same name already exists.")
#     print('\n')


# def move():
#     """This function move document from previous directory to new (main func)"""
#     type_doc = input("Enter a name for the new shelf: ").lower()
#     type_doc_old = input("Enter the name of the current shelf: ").lower()
#     number_doc = input("Enter document number: ")

#     if type_doc in directories.keys():
#         if type_doc_old in directories.keys():
#             for value in directories.values():
#                 if number_doc in value:
#                     move_body(type_doc, type_doc_old, number_doc)
#                     break
#             else:
#                 print("Document with this number does not exist!")
#         else:
#             print("Shelf with this name does not exist!")
#     else:
#         print("Shelf with this name does not exist!")

#     print('\n')


# def move_body(type_doc, type_doc_old, number_doc):
#     """This function move document from previous directory to new (body func)"""

#     if number_doc in directories[type_doc_old]:
#         directories[type_doc_old].remove(number_doc)
#         if directories[type_doc_old] is None:
#             directories[type_doc_old] = []
#         else:
#             pass
#         for key in directories.keys():
#             if key == type_doc:
#                 directories[key].append(number_doc)
#     else:
#         print(f"Document with number {number_doc} is not on the shelf {type_doc_old}")

#     print('\n')
