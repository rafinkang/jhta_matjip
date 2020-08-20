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
        # ["제목", "생성자", "현재인원", "모집인원", "종료시간", "버튼"]
        self.lb_title = QLabel("제목", self)
        self.lb_max_member = QLabel("모집인원", self)
        self.lb_end_time = QLabel("종료시간", self)

        self.le_title = QLineEdit(self)
        self.le_max_member = QLineEdit(self)
        # self.le_end_time = QLineEdit(self)
        self.le_end_time = QDateTimeEdit(self)
        self.le_end_time.setMinimumDateTime(datetime.datetime.now())

        self.btn_new_party = QPushButton("파티생성", self)
        self.btn_back = QPushButton("뒤로", self)

        self.btn_new_party.clicked.connect(self.new_party)
        self.btn_back.clicked.connect(lambda: parent.route_page('party'))

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(self.lb_title, 0, 0)
        grid.addWidget(self.le_title, 0, 1)
        grid.addWidget(self.lb_max_member, 1, 0)
        grid.addWidget(self.le_max_member, 1, 1)
        grid.addWidget(self.lb_end_time, 2, 0)
        grid.addWidget(self.le_end_time, 2, 1)
        
        grid.addWidget(self.btn_new_party, 3, 0)
        grid.addWidget(self.btn_back, 3, 1)
    
    def new_party(self):
        title = self.le_title.text()
        max_member = self.le_max_member.text()
        end_time = self.le_end_time.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        user_id = self.parent.user_id
        user_name = self.parent.user_name + "!" 
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