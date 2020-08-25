import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from classes.DbConn import *
import datetime

class PartyInsert(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.initUI(parent)
        
    def initUI(self, parent):
        self.le_title = QLineEdit(self)
        # self.le_max_member = QLineEdit(self)
        self.le_max_member = QSpinBox(self)
        self.le_max_member.setRange(2,20)
        # self.le_end_time = QLineEdit(self)
        self.le_end_time = QDateTimeEdit(self)
        self.le_end_time.setMinimumDateTime(datetime.datetime.now())

        self.btn_new_party = QPushButton("파티생성", self)
        self.btn_back = QPushButton("뒤로", self)

        self.btn_new_party.clicked.connect(self.new_party)
        self.btn_back.clicked.connect(lambda: parent.route_page('party'))


        self.le_title.setGeometry(610, 155, 150, 25)
        self.le_max_member.setGeometry(610, 220, 150, 25)
        self.le_end_time.setGeometry(610, 280, 150, 25)
        self.btn_new_party.setGeometry(610, 335, 150, 25)
        self.btn_back.setGeometry(610, 390, 150, 25)

        self.btn_new_party.setStyleSheet("background-color: #B06649; color: #FFF; border-radius:10px")
        self.btn_back.setStyleSheet("background-color: #119A19; color: #FFF; border-radius:10px")
    
    def new_party(self):
        title = self.le_title.text()
        # max_member = self.le_max_member.text()
        max_member = self.le_max_member.value()
        end_time = self.le_end_time.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        user_id = self.parent.user_id
        user_name = self.parent.user_name
        # print(title, max_member, end_time)

        db = DbConn()
        q1 = "SELECT * FROM matjip_party WHERE user_id = :user_id AND end_time > SYSDATE AND status = 1"
        res = db.execute(q1, {'user_id' : user_id})
        
        if len(res) == 0 :
            query = """
            INSERT INTO matjip_party 
            (title, user_id, cur_member, max_member, member_list, status, end_time) 
            VALUES (:title, :user_id, 1, :max_member, :member_list, 1, TO_DATE(:end_time, 'yyyy-MM-dd hh24:mi:ss'))
            """
            db.execute(query, {'title' : title, 'user_id': user_id, 'max_member' : max_member, 'member_list' : user_name, 'end_time' : end_time})
            self.alert_msg("모집 등록이 완료되었습니다.")
            self.parent.route_page('party')
        else:
            self.alert_msg("이미 모집중인 파티가 있습니다.")
                
        db.disconnect()
        
    def alert_msg(self, content):
        QMessageBox.question(self,
                "!!!", content, QMessageBox.Yes)