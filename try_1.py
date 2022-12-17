import tkinter as tk
from tkinter import ttk
from data import HELP
# from Function_Class import Manager

documents = []

root = tk.Tk()

itms = ['Print Doc info', 'List of Docs', 'Add Doc info', 'Delete Doc info', 'Open helper']

def choose(event):
    if check.get() == 'Print Doc info':
        pass
    elif check.get() == 'List of Docs':
        lbl = tk.Label(text='List:')
        lbl.pack()

        
        
    elif check.get() == 'Add Doc info':
        number_doc_lbl = tk.Label(root, text='Enter Doc number:')
        number_doc_entr = tk.Entry(root)
        number_doc_lbl.pack()
        number_doc_entr.pack()

        type_doc_lbl = tk.Label(root, text='Enter Doc type:')
        type_doc_entr = tk.Entry(root)
        type_doc_lbl.pack()
        type_doc_entr.pack()

        name_doc_lbl = tk.Label(root, text='Enter Doc name:')
        name_doc_entr = tk.Entry(root)
        name_doc_lbl.pack()
        name_doc_entr.pack()

        # def add_doc(event):
        #     global documents
        #     dict_new = {"type": type_doc_entr.get(), "number": number_doc_entr.get(), "name": name_doc_entr.get()}
        #     documents.append(dict_new)

        btn = tk.Button(root, text='Submit')
        btn.pack()
        # btn.bind('<Button-1>', add_doc)
        
    elif check.get() == 'Delete Doc info':
        pass
    elif check.get() == 'Open helper':
        lbl = tk.Label(text=HELP)
        lbl.pack()

check = ttk.Combobox(root, values=itms)
check_btn = tk.Button(text='Submit')
check_btn.bind('<Button-1>', choose)
check.pack()
check_btn.pack()










root.mainloop()