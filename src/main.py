from tkinter import *
#from functions import openFile
from tkinter.filedialog import askopenfilename, asksaveasfile
import platform
import os


class mainWindow:

    def __init__(self, root):
        self.root = root
        self.file = None
        self.lastFileModified = None
        root.title("Welcome to AERO")

        #main menu
        self.mainMenu = Menu(self.root)
        self.fileMenu = Menu(self.mainMenu, tearoff=0)
        self.editMenu = Menu(self.mainMenu, tearoff=0)

        #adding file menu dropdown options
        self.fileMenu.add_command(label='open', command=self.openFile, accelerator='Ctrl+o')
        self.fileMenu.add_command(label='saveFile', command=self.saveFile, accelerator='Ctrl+s')
        self.fileMenu.add_command(label='saveAsFile', command=self.saveAsFile, accelerator='Ctrl+n')
        self.mainMenu.add_cascade(label='Edit', menu=self.fileMenu,)

        #text editor
        self.numberLine = Text(self.root, width=5, highlightbackground='#212835', bg='#212835', borderwidth=0)
        self.numberLine.pack(side=LEFT, fill='both')

        self.textEditor = Text(self.root, tabs='34', highlightbackground='#212835', bg='#212835', borderwidth=0)
        self.textEditor.pack(fill='both', expand=True)

        #root configuration
        self.root.config(menu=self.mainMenu,)
        #self.root.configure(background='black')
        self.root.bind("<Control-o>", self.openFile)
        self.root.bind("<Control-s>", self.saveFile)
        self.root.bind("<Control-n>", self.saveAsFile)


    #function for opening files
    def _changeTitleName(self, *args, **kwargs):
        self.root.title(self.file.split('/')[-1])

    def openFile(self, *args, **kwargs):
        self.file = askopenfilename(initialdir = "c:/",
                filetypes = (('Python Files', '*.py'),('All Files', '*.*'),),
                title = "Choose a File to open",)
        try:
            with open(self.file, 'r') as fileRead:
                fileR = fileRead.read()
                self.textEditor.insert(INSERT, fileR)
            self._changeTitleName()

        except Exception as e:
            print(e)


    #function for saving files
    def saveFile(self, *args, **kwargs):
        try:
            with open(self.file, 'w') as fileS:
                to_write = self.textEditor.get('1.0', END)
                #print("to_write" + to_write)
                fileS.write(to_write)
            self._changeTitleName()

        except Exception as e:
            print("Exception in saveFile as %s" % e)

    #function for creating or saveAsFile
    def saveAsFile(self,*args, **kwargs):
        to_saveFile = asksaveasfile(
                    initialdir = ('c:/'),
                    filetypes = (('Python Files', '*.py'),('All Files', '*.*')),
                    title = 'Save As',
                    defaultextension = '*.*',
                    )
        self.file = to_saveFile.name
        print(to_saveFile.date_modified)
        self.saveFile()

    #function for writing numbers on text widget



app = Tk()
aero = mainWindow(app)
app.mainloop()
