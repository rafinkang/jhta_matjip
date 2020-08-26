import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from classes.DbConn import *
import datetime

class PartyDetail(QWidget):
    def __init__(self, parent, p_idx):
        super().__init__()
        self.parent = parent
        self.p_idx = p_idx
        self.initUI(parent)
        
    def initUI(self, parent):
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        
        datas = self.get_party_data()
        p_idx, title, create_id, self.cur_mem, self.max_mem, member_list, status, end_time = datas[0]
        self.mem_list = member_list
        self.mem_list = self.mem_list.split(",")
        
        self.btn_refresh = QPushButton("새로고침", self)
        self.btn_party = QPushButton("파티참가", self)
        self.btn_back = QPushButton("뒤로가기", self)
        if self.parent.user_id == create_id:    
            self.btn_party.setText("파티삭제")
            self.btn_party.clicked.connect(self.del_party)
        elif self.parent.user_name in self.mem_list:
            self.btn_party.setText("참가취소")
            self.btn_party.clicked.connect(self.cancel_party)
        else:
            self.btn_party.clicked.connect(self.join_party)

        self.label_title = QLabel("제목 : "+ title, self)
        self.label_user_id = QLabel("파티장 : "+ create_id, self)
        self.label_mem_list = QLabel("파티원 : "+ member_list, self)
        
        # QListWidgetItem()

        self.lineedit_reple = QLineEdit()
        self.btn_reple = QPushButton("댓글달기", self)

        self.layout.addWidget(self.label_title, 0, 0, 1, 1)
        self.layout.addWidget(self.label_user_id, 0, 1, 1, 1)
        self.layout.addWidget(self.btn_party, 0, 2, 1, 1)
        self.layout.addWidget(self.btn_back, 0, 3, 1, 1)

        self.layout.addWidget(self.label_mem_list, 1, 0, 1, 3)

        self.layout.addWidget(self.btn_refresh, 1, 3, 1, 1)
        self.layout.addWidget(self.lineedit_reple, 2, 0, 1, 3)
        self.layout.addWidget(self.btn_reple, 2, 3, 1, 1)
        
        self.create_table()
        
        self.btn_back.clicked.connect(lambda: parent.route_page('party'))
        self.btn_reple.clicked.connect(self.set_reple)
        self.btn_refresh.clicked.connect(lambda: self.parent.route_page('party_detail', self.p_idx))
        
    def keyPressEvent(self, e):
        key = e.key()
        if key == Qt.Key_Enter or key == Qt.Key_Return:
            self.set_reple()
        
        
    
    def connect_detail_btn(self, btn, p_idx):
        btn.clicked.connect(lambda: self.parent.route_page('party_detail', p_idx))
        
    
    def create_table(self):
        self.table = QTableWidget()        
        
        # self.table.setSelectionBehavior(QTableView.SelectRows) # multiple row 선택 가능 
        self.table.setSelectionMode(QAbstractItemView.SingleSelection) 
        
        reple_datas = self.get_party_reple_data()
        # row, column 갯수 설정해야만 tablewidget 사용할수있다. 
        self.table.setColumnCount(3) 
        default_low = 15
        if len(reple_datas) > default_low : default_low = len(reple_datas)
        self.table.setRowCount(default_low) 
        # column header 명 설정. 
        self.table.setHorizontalHeaderLabels(["작성시간", "댓글", "작성자"]) 
        self.table.setColumnWidth(0, 80) #컬럼 사이즈 설정
        self.table.setColumnWidth(1, 550) #컬럼 사이즈 설정
        self.table.setColumnWidth(2, 110) #컬럼 사이즈 설정
        
        row = 0
        for data in reple_datas:
            pr_idx, p_idx, rep_user_id, reple, rep_time, status = data
            
            # cell 에 data 입력하기 
            self.table.setItem(row, 0, QTableWidgetItem(rep_time.strftime('%m-%d %H:%M'))) 
            self.table.setItem(row, 1, QTableWidgetItem(reple)) 
            self.table.setItem(row, 2, QTableWidgetItem(rep_user_id)) 
            
            self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) # edit 금지 모드 
            
            row += 1

        self.layout.addWidget(self.table, 3, 0, 1, 4)
        
    def get_party_data(self):
        db = DbConn()
        query = "SELECT * FROM matjip_party WHERE p_idx = :p_idx"
        datas = db.execute(query, {"p_idx":self.p_idx})
        return datas
    
    def get_party_reple_data(self):
        db = DbConn()
        query = "SELECT * FROM party_reple WHERE p_idx = :p_idx ORDER BY rep_time"
        datas = db.execute(query, {"p_idx":self.p_idx})
        return datas
    
    def set_reple(self):
        reple = self.lineedit_reple.text()
        if reple != '' :
            db = DbConn()
            query = "INSERT INTO party_reple(p_idx, user_id, reple, rep_time, status) VALUES (:p_idx, :user_id, :reple, sysdate, 1)"
            db.execute(query, {"p_idx":self.p_idx, "user_id":self.parent.user_id, "reple":reple})
            self.parent.route_page("party_detail", self.p_idx)
        
    def del_party(self):
        db = DbConn()
        query = "UPDATE matjip_party SET status = 0 WHERE p_idx = :p_idx"
        datas = db.execute(query, {"p_idx":self.p_idx})
        self.alert_msg("파티가 삭제되었습니다.")
        self.parent.route_page("party")

    def cancel_party(self):
        db = DbConn()
        query = "UPDATE matjip_party SET member_list = :member_list , cur_member = cur_member-1 WHERE p_idx = :p_idx"
        self.mem_list.remove(self.parent.user_name)
        member_list = ",".join(self.mem_list)
        db.execute(query, {"member_list": member_list, "p_idx":self.p_idx})
        self.alert_msg("파티 탈퇴 성공 !")
        self.parent.route_page("party_detail", self.p_idx)
    
    def join_party(self):
        db = DbConn()
        query = "UPDATE matjip_party SET member_list = :member_list , cur_member = :cur_member WHERE p_idx = :p_idx"
        cur_member = self.cur_mem
        if  cur_member <= self.max_mem:
            self.mem_list.append(self.parent.user_name)
            member_list = ",".join(self.mem_list)
            cur_member += 1
            db.execute(query, {"member_list": member_list, "cur_member": cur_member, "p_idx":self.p_idx})

            self.alert_msg("파티에 참가하였습니다.")
            self.parent.route_page("party")
        else:
            self.alert_msg("파티가 가득 찼습니다. 메롱~")
            
        
    
    def alert_msg(self, content):
        QMessageBox.question(self,
            "!!!", content, QMessageBox.Yes)