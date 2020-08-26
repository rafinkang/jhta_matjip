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
        self.btn1 = QPushButton("", self)
        self.btn2 = QPushButton("", self)
        self.btn3 = QPushButton("", self)
        self.btn4 = QPushButton("", self)
        self.btn5 = QPushButton("", self)

        icon_matjip  = QIcon('./images/restaurant.png')
        self.btn1.setIcon(icon_matjip)
        self.btn1.resize(175, 260)
        self.btn1.setIconSize(QSize(175, 260))
        self.btn1.setStyleSheet('background-color: transparent')
        icon_cafe  = QIcon('images\cafe.png')
        self.btn2.setIcon(icon_cafe)
        self.btn2.resize(175, 260)
        self.btn2.setIconSize(QSize(175, 260))
        self.btn2.setStyleSheet('background-color: transparent')
        icon_mart  = QIcon('images\mart.png')
        self.btn3.setIcon(icon_mart)
        self.btn3.resize(175, 260)
        self.btn3.setIconSize(QSize(175, 260))
        self.btn3.setStyleSheet('background-color: transparent')
        icon_party  = QIcon('images\party.png')
        self.btn4.setIcon(icon_party)
        self.btn4.resize(175, 260)
        self.btn4.setIconSize(QSize(175, 260))
        self.btn4.setStyleSheet('background-color: transparent')
        icon_logout  = QIcon('images\logout.png')
        self.btn5.setIcon(icon_logout)
        self.btn5.resize(100, 150)
        self.btn5.setStyleSheet('background-color: transparent')
        self.btn5.setIconSize(QSize(50, 75))

        self.btn1.clicked.connect(lambda: parent.route_page('restaurant'))
        self.btn2.clicked.connect(lambda: parent.route_page('cafe'))
        self.btn3.clicked.connect(lambda: parent.route_page('mart'))
        self.btn4.clicked.connect(lambda: parent.route_page('party'))
        self.btn5.clicked.connect(lambda: parent.route_page('login'))

        vbox = QVBoxLayout()
        self.setLayout(vbox)

        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        vbox.addStretch()
        vbox.addLayout(hbox2)

        hbox1.addStretch()
        hbox1.addWidget(self.btn5)

        vbox.addStretch()
        vbox.addLayout(hbox1)
        
        hbox2.addWidget(self.btn1)
        hbox2.addWidget(self.btn2)
        hbox2.addWidget(self.btn3)
        hbox2.addWidget(self.btn4)
        hbox1.addWidget(self.btn5)