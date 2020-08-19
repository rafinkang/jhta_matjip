import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from classes.DbConn import *

class Register(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.initUI(parent)
        
    def initUI(self, parent):
        self.lb2Id = QLabel("ID", self)
        self.lb2Pw = QLabel("PW", self)
        self.lb2Name = QLabel("NAME", self)
        self.le2Id = QLineEdit(self)
        self.le2Pw = QLineEdit(self)
        self.le2Name = QLineEdit(self)
        self.btn = QPushButton("가입하기", self)

        # self.btn.clicked.connect(self.myregister)

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(self.lb2Id, 0, 0)
        grid.addWidget(self.le2Id, 0, 1)
        grid.addWidget(self.lb2Pw, 1, 0)
        grid.addWidget(self.le2Pw, 1, 1)
        grid.addWidget(self.lb2Name, 2, 0)
        grid.addWidget(self.le2Name, 2, 1)
        grid.addWidget(self.btn, 3, 0)