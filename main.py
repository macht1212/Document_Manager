from data import *
import tkinter as tk
from tkinter import ttk



window = tk.Tk()
window.title('Document manager')

items = HELP_list

def people(event):
    """ This function helps to find a person with his document"""

    number_doc = ppl.get()

    for docs in documents:
        docs_arr = list(docs.items())
        number = docs_arr[1][1]
        if number == number_doc in docs_arr[1][1]:
            ppl_lab['text'] = f"The owner of the document with the number {number_doc}: {docs_arr[2][1]}"
            print(f"The owner of the document with the number {number_doc}: {docs_arr[2][1]}")
            break
    else:
        ppl_lab['text'] = "Document with this number does not exist!"
        print("Document with this number does not exist!")
    print('\n')


ppl = tk.Entry()
ppl_btn = tk.Button(text='Print Docs info')
ppl.bind('<Button-1>', people)
ppl_lab = tk.Label(bg='black', fg='white')





def add(event):
    """This function adds new information to documents and directories"""

    name = addinf_input_name.get()
    type_doc = addinf_input_type.get()
    number_doc = addinf_input_num.get()

    dict_new = {"type": type_doc.lower(), "number": number_doc, "name": name}
    documents.append(dict_new)
    addinf_lab['text'] = 'Done'
    print("Done!")
    print('\n')



addinf = tk.Label(text='Add Doc Info')
addinf_type = tk.Label(text='Type')
addinf_input_type = tk.Entry()
addinf_num = tk.Label(text="Doc's number")
addinf_input_num = tk.Entry()
addinf_name = tk.Label(text="Owner's name")
addinf_input_name = tk.Entry()
addinf_btn = tk.Button(text='Submit')
addinf_btn.bind('<Button-1>', add)
addinf_lab = tk.Label(bg='black', fg='white')

lod = tk.Label(text='List of Docs')
lod_btn = tk.Button(text='List of Docs')



ppl.pack()
ppl_btn.pack()
ppl_lab.pack()

addinf.pack()
addinf_type.pack()
addinf_input_type.pack()
addinf_num.pack()
addinf_input_num.pack()
addinf_name.pack()
addinf_input_name.pack()
addinf_btn.pack()
addinf_lab.pack()

lod.pack(side='left')
lod_btn.pack(side='left')



# # Переписать участки на .grid()
# frame_wrap = tk.Frame(window)
# frame_command = tk.Frame(frame_wrap, height=150, bg='green')
# frame_input_info = tk.Frame(frame_wrap, height=150, bg='yellow')


# frame_wrap.pack(fill='both')
# frame_command.pack(side='left', fill='both', expand=True, ipady=60)
# frame_input_info.pack(side='right', fill='both', expand=True, ipady=60)


# l_choose_command = ttk.Label(text='Choose command: ')
# f_choose_command = ttk.Combobox(values=items) 
# btn_submit = ttk.Button(text='Submit')

# l_choose_command.pack(side='top')
# # f_choose_command.grid(row=0, column=1)
# # btn_submit.grid(row=1, column=1)

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