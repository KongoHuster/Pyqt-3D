# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication,  QWidget,QLabel
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout
from test import Ui_MainWindow
class myform(QWidget,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.count)


    def count(self):
        f=self.open(1..txt)
        self.label.setText("%s",f)
        self.close(1..txt)


if __name__ == '__main__':
 app=QApplication(sys.argv)
 w=myform()
 w.show()
 app.exec_()