import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from classes.DbConn import *

class Login(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.initUI(parent)
        
    def initUI(self, parent):
        self.lb_id = QLabel("ID", self)
        self.lb_pw = QLabel("PW", self)
        
        self.le_id = QLineEdit(self)
        self.le_pw = QLineEdit(self)

        self.btn_login = QPushButton("로그인", self)
        self.btn_register = QPushButton("회원가입", self)
        self.btn_findpw = QPushButton("ID/PW찾기", self)

        self.btn_findpw.clicked.connect(lambda: parent.route_page('menu'))
        self.btn_register.clicked.connect(lambda: parent.route_page('register'))

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(self.lb_id, 0, 0)
        grid.addWidget(self.le_id, 0, 1)
        grid.addWidget(self.lb_pw, 1, 0)
        grid.addWidget(self.le_pw, 1, 1)
        grid.addWidget(self.btn_login, 2, 0)
        grid.addWidget(self.btn_register, 2, 1)
        grid.addWidget(self.btn_findpw, 2, 2)