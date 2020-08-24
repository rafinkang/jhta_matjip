import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from classes.DbConn import *

class Login(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        parent.user_id = None
        parent.user_name = None
        self.initUI(parent)
        
    def initUI(self, parent):
        self.le_id = QLineEdit(self)
        self.le_pw = QLineEdit(self)

        self.btn_login = QPushButton("로그인", self)
        self.btn_register = QPushButton("회원가입", self)
        self.btn_findpw = QPushButton("ID/PW찾기", self)

        self.btn_login.clicked.connect(self.login)
        self.btn_findpw.clicked.connect(lambda: parent.route_page('find_id'))
        self.btn_register.clicked.connect(lambda: parent.route_page('register'))


        self.le_id.setGeometry(600,205,150,30)
        self.le_pw.setGeometry(600,275,150,30)
        self.btn_login.setGeometry(600,465,150,30)
        self.btn_register.setGeometry(600,505,150,30)
        self.btn_findpw.setGeometry(600,545,150,30)
        
    def keyPressEvent(self, e):
        key = e.key()
        if key == Qt.Key_Enter or key == Qt.Key_Return:
            self.login()
        
    def login(self):
        user_id = self.le_id.text()
        user_pw = self.le_pw.text()
        
        query = "select name from jhta_user where user_id = :user_id and pwd = :pwd"
        db = DbConn()
        result = db.execute(query, {'user_id' : user_id, 'pwd' : user_pw})
        if len(result) == 0 :
            QMessageBox.question(self,
                "Error!", "아이디 또는 패스워드를 확인해주세요.", QMessageBox.Yes)
        else:
            self.parent.user_name = result[0][0]
            self.parent.user_id = user_id
            self.parent.route_page('menu')