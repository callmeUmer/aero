from tkinter import *
#from .text import textEditor
from .highlight import highlighter
from .menubars import menubar
from .filehandler import filehandler



class connector:
    def __init__(self, main):
        self.main = main
        self.initModules()

    def initModules(self):
        #textEditor(self.main)
        #highlighter(self.main.textEditor)
        menubar(self.main)
        filehandler(self.main)
