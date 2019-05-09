from tkinter import *
#from functions import openFile
from tkinter.filedialog import askopenfilename, asksaveasfile
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

        #number line
        self.scroll = Scrollbar(self.root, orient=VERTICAL, command=self._simulScroll)
        self.scroll.pack()
        self.numberLine = Text(
                self.root, width=5, highlightbackground='#212835', bg='#212835',
                borderwidth=0, highlightthickness=0, fg='white',)
        self.numberLine.pack(side=LEFT, fill='both')
        self.numberLine['yscrollcommand'] = self.scroll.set
        self.numberLine.config(state=DISABLED)

        #text editor
        self.textEditor = Text(
                self.root, tabs='34', highlightbackground='#212835', bg='#212835',
                borderwidth=0, highlightthickness=0, insertbackground='white', fg='white', wrap='none')
        self.textEditor.pack(fill='both', expand=True)
        self.textEditor['yscrollcommand'] = self.scroll.set

        #root configuration
        self.root.config(menu=self.mainMenu,)

        #some key bindings
        self.root.bind("<Control-o>", self.openFile)
        self.root.bind("<Control-s>", self.saveFile)
        self.root.bind("<Control-n>", self.saveAsFile)
        self.textEditor.bind("<BackSpace>", self.writeNumberLine)
        self.textEditor.bind('<Button-5>', self._on_mousewheel_up)
        self.textEditor.bind('<Button-4>', self._on_mousewheel_down)
        self.textEditor.bind('<Up>', self._on_mousewheel_up)
        self.textEditor.bind('<Down>', self._on_mousewheel_down)
        self.numberLine.bind('<Button-5>', self._on_mousewheel_up)
        self.numberLine.bind('<Button-4>', self._on_mousewheel_down)
        self.numberLine.bind('<Up>', self._on_mousewheel_up)
        self.numberLine.bind('<Down>', self._on_mousewheel_down)
        self.textEditor.bind("<Return>", self.writeNumberLine)

    #function for simultanous Scrollbar
    def _simulScroll(self, *args, **kwargs):
        eval('self.textEditor.yview(*args)')
        eval('self.numberLine.yview(*args)')


    def _on_mousewheel_up(self, event):
        self.textEditor.yview_scroll(1, "units")
        self.numberLine.yview_scroll(4, "units")

    def _on_mousewheel_down(self, event):
        self.textEditor.yview_scroll(-1, "units")
        self.numberLine.yview_scroll(-4, "units")


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
            self.writeNumberLine()
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

    def writeNumberLine(self, *event):
        displayLines = self.textEditor.count("1.0", "end", "lines")
        self.numberLine.config(state=NORMAL)
        self.numberLine.delete('1.0', END)
        for item in range(1, displayLines+2):
            self.numberLine.insert(float(item), str(item) + '\n')
        self.numberLine.config(state=DISABLED)


app = Tk()
aero = mainWindow(app)
app.mainloop()
