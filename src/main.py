from tkinter import *
#from functions import openFile
from tkinter.filedialog import askopenfilename, asksaveasfile

#some global variables
file = None


# function to open a file in text editor
def openFile(*args, **kwargs):
    global file
    file = askopenfilename(initialdir = "c:/",
            filetypes = (('Python Files', '*.py'),('All Files', '*.*'),),
            title = "Choose a File to open",)
    try:
        with open(file, 'r') as fileRead:
            fileR = fileRead.read()
            textEditor.insert(INSERT, fileR)

    except Exception as e:
        print(e)

# function to save the content in text editor to an opened file
def saveFile(*args, **kwargs):
    try:
        with open(file, 'w') as fileS:
            to_write = textEditor.get('1.0', END)
            #print("to_write" + to_write)
            fileS.write(to_write)

    except Exception as e:
        print(e)

# function to save the content in text editor to a new file of your desire
def saveAsFile(*args, **kwargs):
    to_saveFile = asksaveasfile(
                initialdir = ('c:/'),
                filetypes = (('Python Files', '*.py'),('All Files', '*.*')),
                title = 'Save As',
                defaultextension = '*.*',
                )
    global file
    file = to_saveFile.name
    saveFile()


window = Tk()

# this part of code initiate main windows
mainFrame = Frame(window)
mainFrame.pack()

# this initiate main menubar at top
menuBar = Menu(window)

# following lines of code will initiate options on menubar
fileMenu = Menu(menuBar, tearoff=0)
editMenu = Menu(menuBar, tearoff=0)

#following block is for filemenu :)
fileMenu.add_command(label='Open', command=openFile, accelerator='Ctrl+o')
fileMenu.add_command(label='Save', command=saveFile, accelerator='Ctrl+s')
fileMenu.add_command(label='SaveAs/newFile', command=saveAsFile, accelerator='Ctrl+n')
menuBar.add_cascade(label='File', menu=fileMenu)

# following block is for editmenu
editMenu.add_command(label='Undo', command='')
editMenu.add_command(label='Redo', command='')
menuBar.add_cascade(label='Edit', menu=editMenu)


#adding a text editor
textEditor = Text(window)
textEditor.pack()

#adding some shortcuts

window.bind("<Control-o>", openFile)
window.bind("<Control-s>", saveFile)
window.bind("<Control-n>", saveAsFile)


window.config(menu=menuBar)
window.mainloop()
