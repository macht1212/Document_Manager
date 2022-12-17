![Document_Manager.png](img/Document_Manager.png)

By Alexander Nazimov


## Introduction 
 
I've started building my own document manager to practice my programming skills.

At the moment, the program is a set of functions that can be used in the console and only while the console is active.

The essence of this program is that you have a set of various document parameters, such as type, number, title, number of pages, etc., as well as the ability to create various shelves that will be named according to the type of document.
The document is saved to a list of dictionaries, which will store all the information in the future, but so far only while the program itself is active.

### **But my plans for this project are huge!**

Now the program is implemented as a set of functions and commands that must be entered into the console.
The list of implemented functions is presented below:

```python
    HELP = """
    p - the command to search for the owner by document number,
    s - the command shows the shelf on which the document is stored,
    l - the command displays all the documents that are in the list,
    a - the command adds information about the new document and its owner, 
    and also adds the document to the desired shelf,
    d - the command removes all information about the document, the owner 
    from the list and removes the document from the shelf,
    as - the command adds a new empty shelf,
    m - the command moves the document to another required shelf shelf
    h - the command will open the list of available commands again,
    exit - the command will terminate the program.
    """
```

I plan in the future to add the ability to save the process as JSON or otherwise to be able to use the program not only while the console is active.
Or use some kind of DBs like SQL or NoSQL (I've not decided yet which DB will works). 

And also I want to transfer all the functionality of the program to a web application using the Django framework and Front-end elements for even more convenient work with the document manager.
And may be use ```tkinter``` lib to create .app file. 

## Contacts
If you have any ideas on how to improve the functionality of the program, then you can contact me via email nasimov.alexander@gmail.com
