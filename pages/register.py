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

        # self.lb_id = QLabel("ID", self)
        # self.lb_pw = QLabel("PW", self)
        # self.lb_name = QLabel("이름", self)
        # self.lb_birth = QLabel("생년월일", self)
        # self.lb_tel = QLabel("전화번호", self)

        self.le_id = QLineEdit(self)
        self.le_id.setGeometry(250,177,170,30)
        self.le_pw = QLineEdit(self)
        self.le_pw.setGeometry(250,220,170,30)
        self.le_name = QLineEdit(self)
        self.le_name.setGeometry(250,262,170,30)
        self.le_birth = QDateEdit(self)
        self.le_birth.setMinimumDateTime(datetime.datetime.now())
        self.le_birth.setGeometry(250,304,170,30)
        self.le_tel = QLineEdit(self)
        self.le_tel.setGeometry(250,345,170,30)
        self.btn_main = QPushButton("BACK", self)
        self.btn_main.setGeometry(710,150,50,50)
        self.btn_main.setStyleSheet('background-color: #A81919;'
                                    'font: bold 11px;'
                                    'border: 3px solid #19090A;'
                                    'border-radius: 20px;')
        self.btn_register = QPushButton("JOIN", self)
        self.btn_register.setGeometry(710,410,50,50)
        self.btn_register.setStyleSheet('background-color: #A81919;'
                                        'font: bold 11px;'
                                        'border: 3px solid #19090A;'
                                        'border-radius: 20px;')

        self.btn_register.clicked.connect(self.regist)
        self.btn_main.clicked.connect(lambda: parent.route_page('login'))

        # hbox = QHBoxLayout()
        # hbox.addStretch(3)
        # hbox.addLayout(grid)
        # hbox.addStretch(5)
        # self.setLayout(hbox)
    
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