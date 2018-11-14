"""
-*- coding: utf-8 -*-
Author : UMAR SOHAIL
DESCRIPTION: Minimalistic, Customizable Code Editor
"""

from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QWidget, QInputDialog,
                             QLineEdit, QFileDialog, QMainWindow, QMessageBox)
from design import Ui_MainWindow


class mainWindow(QMainWindow, Ui_MainWindow):
    """ mainWindow class to display mainwindows and widgets """

    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)
        self.FILENAME = None
        self.initUI()

    # initialization of UI
    def initUI(self):
        self.WindowTitle = "Python Code Editor"
        self.actionOpen.triggered.connect(self.openFileNameDialog)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSave_As.triggered.connect(self.saveAsFileNameDialog)

    # function for opening a file

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(
            self, "Open Files",
            "",
            "All Files (*);;Python Files (*.py);; C++ Files (*.cpp)",
            options=options)
        if filename:
            self.FILENAME = filename
            with open(filename, 'r') as file:
                read_file = file.read()
                self.textEdit.setPlainText(read_file)

    # function for saving changes to the opened file

    def saveFile(self):
        if self.FILENAME:
            with open(self.FILENAME, 'w') as save:
                text = self.textEdit.toPlainText()
                save.write(text)
        else:
            QMessageBox.warning(
                self,
                'No file opened',
                "No file opened",
                QMessageBox.Yes | QMessageBox.No)

    # function for saving changes to a new file

    def saveAsFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save File",
            "",
            "All Files (*);; Python Files (*.py);; C++ Files(*.cpp)",
            options=options)
        split_ex = _.split(' ')
        extension = ''

        if filename:
            if split_ex[0] == 'C++':
                extension += '.cpp'
            elif split_ex[0] == 'Python':
                extension += '.py'
            else:
                pass

            with open(filename + extension, 'w+') as saveAs:
                self.FILENAME = saveAs
                text = self.textEdit.toPlainText()
                saveAs.write(text)
                saveAs.close()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    sim = mainWindow()
    sim.show()
    sys.exit(app.exec_())
