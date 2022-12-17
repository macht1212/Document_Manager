from Function import *
from data import *
import tkinter as tk
from tkinter import ttk



window = tk.Tk()
window.title('Document manager')
window.geometry('500x500')

items = HELP_list

frame_wrap = tk.Frame(window)
frame_command = tk.Frame(frame_wrap, height=150, bg='green')
frame_input_info = tk.Frame(frame_wrap, height=150, bg='yellow')


frame_wrap.pack(fill='both')
frame_command.pack(side='left', fill='both', expand=True, ipady=60)
frame_input_info.pack(side='right', fill='both', expand=True, ipady=60)


l_choose_command = ttk.Label(text='Choose command: ')
f_choose_command = ttk.Combobox(values=items) 
btn_submit = ttk.Button(text='Submit')

window.mainloop()



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