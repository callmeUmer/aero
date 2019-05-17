from tkinter import *
from .text import textEditor
from .highlight import highlighter
from .menubars import menubar
from .filehandler import filehandler




class mainWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.text = textEditor(self)
        self.highlighter = highlighter(self, self.text)
        self.filehandler = filehandler(self, self.text)
        self.menubar = menubar(self)
