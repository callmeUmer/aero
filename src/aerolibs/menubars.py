from tkinter import *

class menubar:
    def __init__(self, root):
        self.root = root
        self.initMenuBar()

    def initMenuBar(self):
        #main menu
        self.mainMenu = Menu(self.root)
        self.fileMenu = Menu(self.mainMenu, tearoff=0)
        self.editMenu = Menu(self.mainMenu, tearoff=0)

        #adding file menu dropdown options
        self.fileMenu.add_command(label='open', command=self.root.filehandler.openFile, accelerator='Ctrl+o')
        self.fileMenu.add_command(label='saveFile', command=self.root.filehandler.saveFile, accelerator='Ctrl+s')
        self.fileMenu.add_command(label='saveAsFile', command=self.root.filehandler.saveAsFile, accelerator='Ctrl+n')
        self.mainMenu.add_cascade(label='Edit', menu=self.fileMenu,)

        #root configuration
        self.root.config(menu=self.mainMenu,)
