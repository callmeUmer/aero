from tkinter import *
#from functions import openFile
from tkinter.filedialog import askopenfilename


window = Tk()

# this part of code initiate main windows
mainFrame = Frame(window)
mainFrame.pack()

# this initiate main menubar at top
menuBar = Menu(window)

# following lines of code will initiate options on menubar
fileMenu = Menu(menuBar, tearoff=0)
editMenu = Menu(menuBar, tearoff=0)

#following block is for filemenu :)
fileMenu.add_command(label='Open', command=openFile)
fileMenu.add_command(label='New File', command='')
fileMenu.add_command(label='Save', command='')
fileMenu.add_command(label='SaveAs', command='')
menuBar.add_cascade(label='File', menu=fileMenu)

# following block is for editmenu
editMenu.add_command(label='Undo', command='')
editMenu.add_command(label='Redo', command='')
menuBar.add_cascade(label='Edit', menu=editMenu)


#adding a text editor
textEditor = Text(window)
textEditor.pack()




window.config(menu=menuBar)
window.mainloop()
