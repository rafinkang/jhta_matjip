import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from classes.DbConn import *
import datetime

class Party(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.initUI(parent)
        
    def initUI(self, parent):
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.btn_new_party = QPushButton("파티생성", self)
        self.btn_new_party.setStyleSheet("background-color:#119A19; padding:10px; border-radius:10px; color: #fff;")
        self.btn_back = QPushButton("뒤로가기", self)
        self.btn_back.setStyleSheet("background-color:#B06649; padding:10px; border-radius:10px; color: #fff;")
        
        self.layout.addWidget(self.btn_new_party, 0, 0)
        self.layout.addWidget(self.btn_back, 0, 1)
        self.create_table()
        
        self.btn_new_party.clicked.connect(lambda: parent.route_page('party_insert'))
        self.btn_back.clicked.connect(lambda: parent.route_page('menu'))
        
        
    
    def connect_detail_btn(self, btn, p_idx):
        btn.clicked.connect(lambda: self.parent.route_page('party_detail', p_idx))
        
    
    def create_table(self):
        self.table = QTableWidget()        
        
        # self.table.setSelectionBehavior(QTableView.SelectRows) # multiple row 선택 가능 
        self.table.setSelectionMode(QAbstractItemView.SingleSelection) 
        
        datas = self.select_data()
        # row, column 갯수 설정해야만 tablewidget 사용할수있다. 
        self.table.setColumnCount(6)
        default_low = 16
        if len(datas) > default_low : default_low = len(datas)
        self.table.setRowCount(default_low)
        # column header 명 설정. 
        self.table.setHorizontalHeaderLabels(["제목", "생성자", "현재인원", "모집인원", "종료시간", "버튼"]) 
        
        btn_list = []
        row = 0
        for data in datas:
            p_idx = data[0]
            title = data[1] 
            p_user_id = data[2] 
            cur_mem = str(data[3])
            max_mem = str(data[4])
            end_time = data[7] 

            # cell 에 data 입력하기 
            self.table.setItem(row, 0, QTableWidgetItem(title)) 
            self.table.setItem(row, 1, QTableWidgetItem(p_user_id)) 
            self.table.setItem(row, 2, QTableWidgetItem(cur_mem)) 
            self.table.setItem(row, 3, QTableWidgetItem(max_mem)) 
            self.table.setItem(row, 4, QTableWidgetItem(end_time.strftime('%m-%d %H:%M'))) 
            # self.table.setItem(row, 5, QTableWidgetItem("참가버튼")) 
            
            party_btn = QPushButton("파티보기") 
            party_btn.setStyleSheet("background-color:#DF8D6C; border-radius:7px; color: #fff;")
            btn_list.append([party_btn, p_idx])
            self.table.setCellWidget(row, 5, party_btn) 
            
            self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) # edit 금지 모드 
            self.table.setColumnWidth(0, 305) #컬럼 사이즈 설정
            self.table.setColumnWidth(2, 75) #컬럼 사이즈 설정
            self.table.setColumnWidth(3, 75) #컬럼 사이즈 설정
            
            row += 1

        self.layout.addWidget(self.table, 1, 0, 1,2)
        
        for btn, p_idx in btn_list:
            self.connect_detail_btn(btn, p_idx)
        
    def select_data(self):
        db = DbConn()
        query = "SELECT * FROM matjip_party WHERE status = 1 and end_time > sysdate"
        datas = db.execute(query)
        return datas