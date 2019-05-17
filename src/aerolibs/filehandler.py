from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfile
from tkinter import messagebox


class filehandler:
    def __init__(self, root):
        self.root = root
        self.file = None
        self.root.bind("<Control-o>", self.openFile)
        self.root.bind("<Control-s>", self.saveFile)
        self.root.bind("<Control-n>", self.saveAsFile)

    def _changeTitleName(self, *args, **kwargs):
        self.root.title(self.file.split('/')[-1])


    def openFile(self, *args, **kwargs):
        self.file = askopenfilename(initialdir = "c:/",
                filetypes = (('Python Files', '*.py'),('All Files', '*.*'),),
                title = "Choose a File to open",)
        try:
            with open(self.file, 'r') as fileRead:
                fileR = fileRead.read()
                self.textEditor.delete('1.0', END)
                self.textEditor.insert(INSERT, fileR)
            self._changeTitleName()
            self.highlightFile()
        except Exception as e:
            print(e)


    #function for saving files
    def saveFile(self, *args, **kwargs):
        if self.file is None:
            messagebox.showerror("No file is opened", "No file is opened")
        else:
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
