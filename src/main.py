"""
-*- coding: utf-8 -*-
Author : UMAR SOHAIL
DESCRIPTION: Minimalistic, Customizable Code Editor
"""

from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QWidget, QInputDialog, QWidget,
                    QLineEdit, QFileDialog, QMainWindow, QMessageBox, QTabWidget)
from design import Ui_MainWindow
import json


class tabs(QTabWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        super(tabs, self).__init__(parent)
        self.initTab()

    def initTab(self):
        self.tabWidget = QTabWidget()
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName("tab")


class mainWindow(QMainWindow, Ui_MainWindow):
    """ mainWindow class to display mainwindows and widgets """

    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)
        #self.connector()
        self.FILENAME = None
        self.setWindowTitle("Aero")
        self.initUI()
        self.initStyle()

    # initialization of UI
    def initUI(self):
        self.actionOpen.triggered.connect(self.openFileNameDialog)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSaveAs.triggered.connect(self.saveAsFileNameDialog)

    #
    def initStyle(self):
        with open("../config.json", "r") as config:
            configRead = config.read()
            self.jsonData = json.loads(configRead)
            self.backgroundcolor = self.jsonData["editor"][0]["editorBackgroundColor"]
            self.setStyleSheet("QMainWindow{background-color: %s;}" %(self.backgroundcolor))
            self.textEdit_2.setStyleSheet("background-color: %s;" %(self.backgroundcolor))
            self.textEdit.setStyleSheet("background-color: %s;" %(self.backgroundcolor))

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
            if self.FILENAME:
                newtab = tabs()
            self.FILENAME = filename
            self.setWindowTitle(str(filename))
            with open(filename, 'r') as file:
                read_file = file.read()
                self.textEdit.setPlainText(read_file)
                number = 1
                for ln_number, no in enumerate(file):
                    pass
                    number = ln_number
                self.textEdit_2.setPlainText(str(number))


    def newTab(self):
        openTab = tabs()
        widget.exec_()

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
                QMessageBox.Ok)


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
