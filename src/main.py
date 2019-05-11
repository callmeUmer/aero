from tkinter import *
#from functions import openFile
from tkinter.filedialog import askopenfilename, asksaveasfile
from pygments import lex
from pygments.lexers import PythonLexer
import platform
import os


def count_monkeypatch(self, index1, index2, *args):
    args = [self._w, "count"] + ["-" + arg for arg in args] + [index1, index2]
    result = self.tk.call(*args)
    return result

Text.count = count_monkeypatch


class mainWindow(Tk):

    def __init__(self, root):
        self.root = root
        self.file = None
        self.lastFileModified = None
        self.lines = None
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
        self.textEditor = Text(
                self.root, tabs='34', highlightbackground='#212835', bg='#212835',
                borderwidth=0, highlightthickness=0, insertbackground='white', fg='white', wrap='none',)
        self.textEditor.pack(fill='both', expand=True)
        self.textEditor.tag_configure("Token.Keyword", foreground="#CC7A00")
        self.textEditor.tag_configure("Token.Keyword.Constant", foreground="#CC7A00")
        self.textEditor.tag_configure("Token.Keyword.Declaration", foreground="#CC7A00")
        self.textEditor.tag_configure("Token.Keyword.Namespace", foreground="#CC7A00")
        self.textEditor.tag_configure("Token.Keyword.Pseudo", foreground="#CC7A00")
        self.textEditor.tag_configure("Token.Keyword.Reserved", foreground="#CC7A00")
        self.textEditor.tag_configure("Token.Keyword.Type", foreground="#CC7A00")

        self.textEditor.tag_configure("Token.Name.Class", foreground="#003D99")
        self.textEditor.tag_configure("Token.Name.Exception", foreground="#003D99")
        self.textEditor.tag_configure("Token.Name.Function", foreground="#003D99")

        self.textEditor.tag_configure("Token.Operator.Word", foreground="#CC7A00")

        self.textEditor.tag_configure("Token.Comment", foreground="#B80000")

        self.textEditor.tag_configure("Token.Literal.String", foreground="#248F24")

        #root configuration
        self.root.config(menu=self.mainMenu,)

        #some key bindings
        self.root.bind("<Control-o>", self.openFile)
        self.root.bind("<Control-s>", self.saveFile)
        self.root.bind("<Control-n>", self.saveAsFile)
        self.textEditor.bind("<KeyRelease>", self.highlightLine)


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
                self.textEditor.delete('1.0', END)
                self.textEditor.insert(INSERT, fileR)
            self._changeTitleName()
            self.highlightFile()
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


    def highlightLine(self, *args, **kwargs):
        display = self.textEditor.count("1.0", "end", "lines")
        cursor = self.textEditor.index(INSERT)
        cursorSplit = cursor.split('.')
        line = cursorSplit[0]
        column = cursorSplit[1]
        lineContext = self.textEditor.get(float(str(line) + '.0'), float(cursor))
        self.textEditor.mark_set("range_start", str(line) + '.0')
        for token, context in lex(lineContext, PythonLexer()):
            print(f'Token is {token} and Context is {context}')


            self.textEditor.mark_set("range_end", "range_start + %dc" % len(context))
            self.textEditor.tag_add(str(token), "range_start", "range_end")
            self.textEditor.mark_set("range_start", "range_end")




app = Tk()
aero = mainWindow(app)
app.mainloop()
