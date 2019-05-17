from tkinter import *
#from functions import openFile
from aerolibs import text



class mainWindow(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, *kwargs)
        self.run()

    def run(self):
        text.textEditor(self)





#app = Tk()
#aero = mainWindow(app)
#app.mainloop()
