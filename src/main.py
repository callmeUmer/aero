from tkinter import *
#from functions import openFile
from tkinter.filedialog import askopenfilename, asksaveasfile
from pygments import lex
from pygments.lexers import PythonLexer, get_lexer_for_filename
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
        self.lexer = None
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
        self.textEditor.tag_configure("Token.Keyword", foreground='#c678dd')
        self.textEditor.tag_configure("Token.Keyword.Constant", foreground='#c678dd')
        self.textEditor.tag_configure("Token.Keyword.Declaration", foreground='#c678dd')
        self.textEditor.tag_configure("Token.Keyword.Namespace", foreground='#c678dd')
        self.textEditor.tag_configure("Token.Keyword.Pseudo", foreground='#c678dd')
        self.textEditor.tag_configure("Token.Keyword.Reserved", foreground='#c678dd')
        self.textEditor.tag_configure("Token.Keyword.Type", foreground='#c678dd')

        self.textEditor.tag_configure("Token.Name.Class", foreground='#e5c07b')
        self.textEditor.tag_configure("Token.Name.Exception", foreground="#003D99")
        self.textEditor.tag_configure("Token.Name.Function", foreground='#61afef')
        self.textEditor.tag_configure("Token.Name.Function.Magic", foreground='#61afef')
        self.textEditor.tag_configure("Token.Name.Builtin", foreground='#56b6c2')
        self.textEditor.tag_configure("Token.Operator.Word", foreground='#c678dd')
        self.textEditor.tag_configure("Token.Comment.Single", foreground='#5c6370')
        self.textEditor.tag_configure("Token.Literal.String.Single", foreground="#248F24")
        self.textEditor.tag_configure("Token.Literal.String.Doc", foreground="#248F24")
        self.textEditor.tag_configure("Token.Literal.String.Double", foreground="#248F24")

        self.textEditor.tag_configure("function", foreground="#CC7A00")

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

    #function to highlight the working line
    def highlightLine(self, *args, **kwargs):
        display = self.textEditor.count("1.0", "end", "lines")
        cursor = self.textEditor.index(INSERT)
        cursorSplit = cursor.split('.')
        line = cursorSplit[0]
        column = cursorSplit[1]
        lineContext = self.textEditor.get(float(str(line) + '.0'), float(cursor))
        self.textEditor.mark_set("range_start", str(line) + '.0')
        #if self.lexer:
        #le = CustomPythonLexer()

        for token, context in lex(lineContext, PythonLexer()):
            print(token , context)
            self.textEditor.mark_set("range_end", "range_start + %dc" % len(context))
            self.textEditor.tag_add(str(token), "range_start", "range_end")
            self.textEditor.mark_set("range_start", "range_end")
        #else:
        #    pass


    #function called when new file is opened
    def highlightFile(self, *args, **kwargs):
        to_highliget = self.textEditor.get('1.0', 'end-1c')
        self.textEditor.mark_set("range_start", '1.0')
        lexerToUse = get_lexer_for_filename(str(self.file))
        self.lexer = lexerToUse

        for token, context in lex(to_highliget, lexerToUse):
            #print(token, context)
            self.textEditor.mark_set("range_end", "range_start + %dc" % len(context))
            self.textEditor.tag_add(str(token), "range_start", "range_end")
            self.textEditor.mark_set("range_start", "range_end")



app = Tk()
aero = mainWindow(app)
app.mainloop()

