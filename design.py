#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(240, 345)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.TextEdit = QtGui.QTextEdit(self.centralwidget)
        self.TextEdit.setReadOnly(True)
        self.TextEdit.setObjectName(_fromUtf8("TextEdit"))
        self.verticalLayout.addWidget(self.TextEdit)
        self.btnProcess = QtGui.QPushButton(self.centralwidget)
        self.btnProcess.setObjectName(_fromUtf8("btnProcess"))
        self.verticalLayout.addWidget(self.btnProcess)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))


        self.statusBar()
        mainMenu = self.menuBar()
        openFile = QtGui.QAction("&Open File", self)
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(openFile)

        self.btnProcess.setText(_translate("MainWindow", "Process", None))
