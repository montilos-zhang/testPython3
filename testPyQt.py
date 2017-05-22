#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        exitGUI = QApplication.style().standardIcon(QStyle.SP_TitleBarCloseButton)
        exitAction = QAction(exitGUI, '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        qtInfoGUI = QApplication.style().standardIcon(QStyle.SP_TitleBarMenuButton)
        qtInfoAction = QAction(qtInfoGUI, '&AboutQt', self)
        qtInfoAction.setShortcut('Ctrl+I')
        qtInfoAction.setStatusTip('Show Qt info')
        qtInfoAction.triggered.connect(qApp.aboutQt)

        fileGUI = QApplication.style().standardIcon(QStyle.SP_TitleBarNormalButton)
        fileAction = QAction(fileGUI,'&File',self)
        fileAction.setShortcut('Ctrl+F')
        fileAction.setStatusTip('Show File info')
        fileAction.triggered.connect(qApp.aboutQt)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Info')
        fileMenu.addAction(qtInfoAction)
        fileMenu.addAction(exitAction)
        fileMenu.addAction(fileAction)
        menubar.setNativeMenuBar(False)  # for mac

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()