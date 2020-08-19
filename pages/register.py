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
        self.lb_id = QLabel("ID", self)
        self.lb_pw = QLabel("PW", self)
        self.lb_name = QLabel("이름", self)
        self.lb_birth = QLabel("생년월일", self)
        self.lb_tel = QLabel("전화번호", self)

        self.le_id = QLineEdit(self)
        self.le_pw = QLineEdit(self)
        self.le_name = QLineEdit(self)
        self.le_birth = QLineEdit(self)
        self.le_tel = QLineEdit(self)

        self.btn_register = QPushButton("가입하기", self)
        self.btn_main = QPushButton("뒤로", self)

        self.btn_register.clicked.connect(self.regist)
        self.btn_main.clicked.connect(lambda: parent.route_page('login'))

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(self.lb_id, 0, 0)
        grid.addWidget(self.le_id, 0, 1)
        grid.addWidget(self.lb_pw, 1, 0)
        grid.addWidget(self.le_pw, 1, 1)
        grid.addWidget(self.lb_name, 2, 0)
        grid.addWidget(self.le_name, 2, 1)
        grid.addWidget(self.lb_birth, 3, 0)
        grid.addWidget(self.le_birth, 3, 1)
        grid.addWidget(self.lb_tel, 4, 0)
        grid.addWidget(self.le_tel, 4, 1)
        grid.addWidget(self.btn_register, 5, 0)
        grid.addWidget(self.btn_main, 5, 1)
    
    def regist(self):
        user_id = self.le_id.text()
        pwd = self.le_pw.text()
        name = self.le_name.text()
        birth = self.le_birth.text()
        tel = self.le_tel.text()

        db = DbConn()
        q1 = "select * from jhta_user where user_id = :user_id"
        res = db.execute(q1, {'user_id' : user_id})
        if len(res) == 0 :
            query = "INSERT INTO JHTA_USER (user_id, pwd, name, birth, tel) VALUES (:user_id, :pwd, :name, :birth, :tel)"
            db.execute(query, {'user_id': user_id, 'pwd' : pwd, 'name' : name, 'birth' : birth, 'tel' : tel})
        else:
            QMessageBox.question(self,
                "Error!", "사용 할 수 없는 아이디 입니다.", QMessageBox.Yes)
                
        db.disconnect()
        