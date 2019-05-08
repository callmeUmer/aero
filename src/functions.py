from tkinter import *
from tkinter.filedialog import askopenfilename
#from main import textEditor


#function for opening files
def openFile():
    file = askopenfilename(initialdir = "c:/",
            filetypes = (('Python Files', '*.py'),('All Files', '*.*'),),
            title = "Choose a File to open",)

    try:
        with open(file, 'r') as fileRead:
            fileR = fileRead.read()
            #textEditor.insert(fileR)

    except Exception:
        print("NO FILE EXIST")



