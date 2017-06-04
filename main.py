from __future__ import print_function

from PyQt4 import QtGui  

import sys  
import argparse
import design  # MainWindow related stuff 

# it also keeps events etc that we defined in Qt Designer
import os  # For listing directory methods


class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    name = ""
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.btnProcess.clicked.connect(self.doStuff)  # Call function doStuff when the button is pressed

    def doStuff(self):

        # your code here

        return
    # Shows output of file in TextEdit
    # Fill free to remove it if it is not needed 
    def file_open(self):
        self.name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        file = open(self.name,'r')
        with file:
            text = file.read()
            self.TextEdit.setText(text)

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()
    form.show()  # Show the form
    app.exec_()  # Execute the app


if __name__ == '__main__':
    main()  # run the main function
