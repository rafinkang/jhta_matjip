import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from classes.DbConn import *

class Menu(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.initUI(parent)
        
    def initUI(self, parent):
        self.btn1 = QPushButton("맛집", self)
        self.btn2 = QPushButton("카페", self)
        self.btn3 = QPushButton("이마트", self)
        self.btn4 = QPushButton("파티찾기", self)
        self.btn5 = QPushButton("로그아웃", self)

        self.btn1.clicked.connect(lambda: parent.route_page('restaurant'))
        self.btn2.clicked.connect(lambda: parent.route_page('cafe'))
        self.btn3.clicked.connect(lambda: parent.route_page('mart'))
        self.btn4.clicked.connect(lambda: parent.route_page('party'))
        self.btn5.clicked.connect(lambda: parent.route_page('login'))

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(self.btn1, 0, 0)
        grid.addWidget(self.btn2, 0, 1)
        grid.addWidget(self.btn3, 1, 0)
        grid.addWidget(self.btn4, 1, 1)
        grid.addWidget(self.btn5, 2, 1)