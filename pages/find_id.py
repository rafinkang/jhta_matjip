import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from classes.DbConn import *
import datetime

class FindId(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.initUI(parent)
        
    def initUI(self, parent):
        # self.lb_name = QLabel("이름", self)
        # self.lb_birth = QLabel("생년월일", self)
        
        self.le_name = QLineEdit(self)
        self.le_birth = QDateEdit(self)
        # self.le_birth.setMaximumDate(datetime.datetime.now())

        self.btn_find = QPushButton("찾기", self)
        self.btn_back = QPushButton("뒤로가기", self)

        self.btn_find.clicked.connect(self.find)
        self.btn_back.clicked.connect(lambda: parent.route_page('login'))

        self.btn_find.setStyleSheet("background-color: #774739; color: #FFDE8D; border-radius: 10px;")
        self.btn_back.setStyleSheet("background-color: #26B798; color: #4C3628; border-radius: 10px;")

        self.le_name.setGeometry(350, 170, 100, 25)
        self.le_birth.setGeometry(350, 235, 100, 25)
        self.btn_find.setGeometry(350, 300, 100, 25)
        self.btn_back.setGeometry(350, 365, 100, 25)

        # grid = QGridLayout()
        # self.setLayout(grid)

        # grid.addWidget(self.lb_name, 0, 0)
        # grid.addWidget(self.le_name, 0, 1)
        # grid.addWidget(self.lb_birth, 1, 0)
        # grid.addWidget(self.le_birth, 1, 1)
        # grid.addWidget(self.btn_find, 2, 0)
        # grid.addWidget(self.btn_back, 2, 1)
        
    def find(self):
        name = self.le_name.text()
        if name == '': 
            self.alert_msg("이름을 입력하세요.") 
            return False
        birth = self.le_birth.text()
        if birth == '':
            self.alert_msg("생년월일을 입력하세요.") 
            return False
        
        db = DbConn()
        q1 = "select user_id, pwd from jhta_user where name = :name and birth = :birth"
        result = db.execute(q1, {'birth' : birth, 'name' : name})
        if len(result) > 0:
            self.alert_msg("ID : "+ result[0][0] + " PW : " + result[0][1])
            self.parent.route_page("login")
        else:
            self.alert_msg("해당 정보가 없습니다.")
        
    def alert_msg(self, content):
        QMessageBox.question(self,
            "!!!", content, QMessageBox.Yes)