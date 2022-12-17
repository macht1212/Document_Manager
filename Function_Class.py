from data import documents
# from main import *

class Manager:

    def __init__(self, number_doc, name, type_doc):
        self.number_doc = number_doc
        self.name = name
        self.type_doc = type_doc


    def people(self):
        """ This method helps to find a person with his document"""

        self.number_doc = ppl.get()

        for docs in documents:
            docs_arr = list(docs.items())
            number = docs_arr[1][1]
            if number == self.number_doc in docs_arr[1][1]:
                return f"The owner of the document with the number {self.number_doc}: {docs_arr[2][1]}"
                break
        else:
            return "Document with this number does not exist!"

    
    def list_doc(self):
        """This method shows all list of documents"""

        if documents == []:
            return 'Data is empty! Create somthing with command "a".'
        else:
            for docs in documents:
                return f"Document type: {docs['type']}, document number: {docs['number']}, owner name: {docs['name']}"
    
    def add(self):
        """This method adds new information to documents and directories"""

        dict_new = {"type": self.type_doc.lower(), "number": self.number_doc, "name": self.name}
        documents.append(dict_new)
        

    def delete(self):
        """This function removes all information from documents and directories"""

        for doc in documents:
            docs_arr = list(doc.items())
            if self.number_doc == docs_arr[1][1]:
                documents.remove(doc)
                return f"All information about document number {self.number_doc} has been removed."
                break
        else:
            return "Document with this number does not exist!"
