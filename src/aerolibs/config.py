from tkinter import *
#from .text import textEditor
from .highlight import highlighter
from .menubars import menubar
from .filehandler import filehandler



class connector:
    def __init__(self, main, text):
        self.main = main
        self.text = text
        self.initModules()

    def initModules(self):
        highlighter(self.text)
        filehandler(self.main, self.text)
