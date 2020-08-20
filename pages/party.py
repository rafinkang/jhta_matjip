import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from classes.DbConn import *

class Party(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.initUI(parent)
        
    def initUI(self, parent):
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.btn_new_party = QPushButton("파티생성", self)
        self.btn_back = QPushButton("뒤로가기", self)
        self.layout.addWidget(self.btn_new_party, 0, 0)
        self.layout.addWidget(self.btn_back, 0, 1)
        self.create_table()
        
        self.btn_back.clicked.connect(lambda: parent.route_page('menu'))
    
    def create_table(self):
        self.table = QTableWidget()        
        
        # self.table.setSelectionBehavior(QTableView.SelectRows) # multiple row 선택 가능 
        self.table.setSelectionMode(QAbstractItemView.SingleSelection) 
        
        # row, column 갯수 설정해야만 tablewidget 사용할수있다. 
        self.table.setColumnCount(6) 
        self.table.setRowCount(17) 
        # column header 명 설정. 
        self.table.setHorizontalHeaderLabels(["제목", "생성자", "현재인원", "모집인원", "종료시간", "버튼"]) 
        
        for row in range(17):
            # cell 에 data 입력하기 
            self.table.setItem(row, 0, QTableWidgetItem("순대국 먹으러 갈 사람 모집~~~")) 
            self.table.setItem(row, 1, QTableWidgetItem("taeuk")) 
            self.table.setItem(row, 2, QTableWidgetItem("1")) 
            self.table.setItem(row, 3, QTableWidgetItem("5")) 
            self.table.setItem(row, 4, QTableWidgetItem("08/20-13:00")) 
            # self.table.setItem(row, 5, QTableWidgetItem("참가버튼")) 
            item_widget = QPushButton("참가버튼") 
            self.table.setCellWidget(row, 5, item_widget) 
            
            self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) # edit 금지 모드 
            self.table.setColumnWidth(0, 300) #컬럼 사이즈 설정
            self.table.setColumnWidth(2, 75) #컬럼 사이즈 설정
            self.table.setColumnWidth(3, 75) #컬럼 사이즈 설정

        self.layout.addWidget(self.table, 1, 0, 1,2)