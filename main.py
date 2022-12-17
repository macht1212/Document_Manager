from data import *
import tkinter as tk
from tkinter import ttk
from Function_Class import Manager 



window = tk.Tk()
window.title('Document manager')

items = HELP_list


number_doc_lbl = tk.Label(window, text="Enter Doc number:")
number_doc_entr = tk.Entry(window)
nunber_doc_btn = tk.Button(window, text='Submit')
nunber_doc_btn.bind('<Button-1>', )

name_doc_lbl = tk.Label(window, text="Enter Doc name:")
name_doc_entr = tk.Entry(window)
name_doc_btn = tk.Button(window, text='Submit')
name_doc_btn.bind('<Button-1>', )

type_doc_lbl = tk.Label(window, text="Enter Doc number:")
type_doc_entr = tk.Entry(window)
type_doc_btn = tk.Button(window, text='Submit')
type_doc_btn.bind('<Button-1>', )



manager = Manager(number_doc=number_doc_entr.get(), type_doc=type_doc_entr.get(), name=name_doc_entr.get())




# В данной версии попробую сделать более юзабельный пользовательский интерфейс на основе встроенной библиотеки Tkinter 


# helper = input("Do you need a list of available features? (Y/N): ")
# if helper.lower() == "y":
#     print("The list of commands: \n", HELP)

# while True:
#     command = input("Enter command: ").lower()
#     if command == "p":
#         people()
#     elif command == "s":
#         shelf()
#     elif command == "l":
#         list_doc() 
#     elif command == "a":
#         add()
#     elif command == "d":
#         delete()
#     elif command == "as":
#         add_shelf()
#     elif command == "m":
#         print("Available shelves: \n")
#         for key in directories.keys():
#             print(key.capitalize())
#         print()
#         move()
#     elif command == "h":
#         print("The list of commands: \n", HELP)
#     elif command == "exit":
#         exit()
#     else:
#         print("There is no such command in the list")