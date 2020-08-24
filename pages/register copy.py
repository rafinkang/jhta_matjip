import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from classes.DbConn import *
import datetime

class Register(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.initUI(parent)
        
    def initUI(self, parent):
        self.lb = QLabel('배경',self)
        bg_img = QPixmap('E:/dev/jhta_matjip/images/register_type.jpg')
        self.lb.setPixmap(bg_img)
        self.lb.setGeometry(0,0,800,600)

        self.lb_id = QLabel("ID", self)
        self.lb_pw = QLabel("PW", self)
        self.lb_name = QLabel("이름", self)
        self.lb_birth = QLabel("생년월일", self)
        self.lb_tel = QLabel("전화번호", self)

        self.le_id = QLineEdit(self)
        self.le_pw = QLineEdit(self)
        self.le_name = QLineEdit(self)
        # self.le_birth = QLineEdit(self)
        self.le_birth = QDateEdit(self)
        self.le_birth.setMinimumDateTime(datetime.datetime.now())
        self.le_tel = QLineEdit(self)

        self.btn_register = QPushButton("가입하기", self)
        self.btn_main = QPushButton("뒤로", self)

        self.btn_register.clicked.connect(self.regist)
        self.btn_main.clicked.connect(lambda: parent.route_page('login'))

        grid = QGridLayout()
        grid.setRowStretch(0, 10);
        grid.setRowStretch(4, 10);

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
        grid.addWidget(self.btn_register, 5, 0, 1, 2)
        grid.addWidget(self.btn_main, 6, 0, 1, 2)
        
        hbox = QHBoxLayout()
        hbox.addStretch(3)
        hbox.addLayout(grid)
        hbox.addStretch(5)
        self.setLayout(hbox)
    
    def regist(self):
        user_id = self.le_id.text()
        if user_id == '': 
            self.alert_msg("아이디를 입력해주세요.")
            return False
        pwd = self.le_pw.text()
        if pwd == '': 
            self.alert_msg("비밀번호를 입력해주세요.") 
            return False
        name = self.le_name.text()
        if name == '': 
            self.alert_msg("이름을 입력해주세요.")
            return False
        birth = self.le_birth.text()
        if birth == '': 
            self.alert_msg("생년월일을 입력해주세요.")
            return False
        tel = self.le_tel.text()
        if tel == '': 
            self.alert_msg("전화번호를 입력해주세요.")
            return False

        db = DbConn()
        q1 = "select * from jhta_user where user_id = :user_id"
        res = db.execute(q1, {'user_id' : user_id})
        if len(res) == 0 :
            query = "INSERT INTO JHTA_USER (user_id, pwd, name, birth, tel) VALUES (:user_id, :pwd, :name, :birth, :tel)"
            db.execute(query, {'user_id': user_id, 'pwd' : pwd, 'name' : name, 'birth' : birth, 'tel' : tel})
            self.alert_msg("회원가입이 완료되었습니다.")
            self.parent.route_page('login')
        else:
            self.alert_msg("사용 할 수 없는 아이디 입니다.")
                
        db.disconnect()
        
    def alert_msg(self, content):
        QMessageBox.question(self,
                "!!!", content, QMessageBox.Yes)