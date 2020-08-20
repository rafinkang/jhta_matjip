import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import random
import cx_Oracle
from classes.DbConn import *
from selenium import webdriver


class CafeRe(QWidget):
    def __init__(self, parent, idx):
        super().__init__(parent)
        # print(idx)
        # self.parent = parent       # 각 함수에서 필요한 매개변수를 지정했으므로 전역변수화 필요 없음       
        self.idx = idx         # -> self.로 전역변수 처리하면 각 함수에 매개변수 지정 안 해도 됨
        self.initUI(parent, idx)


    def initUI(self, parent, idx):
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.btn_back = QPushButton("뒤로가기", self)
        self.layout.addWidget(self.btn_back, 0, 1)

        self.rnlb = QLabel(self.bring_info(self.idx)[0][0], self)       # 리스트 0번째 튜플의 0번째 것
        self.btn_site = QPushButton("사이트 바로 가기", self)
        self.layout.addWidget(self.rnlb, 1, 0)
        self.layout.addWidget(self.btn_site, 1, 1)

        self.btn_back.clicked.connect(lambda: parent.route_page('cafe'))
        self.btn_site.clicked.connect(self.go_site)
        self.maketable(idx)


    def go_site(idx):
        url = 'https://store.naver.com/restaurants/detail?entry=pll&id='+str(idx)
        browser = webdriver.Chrome('e:/dev/python_workspace/chromedriver.exe')
        print(url)


    def bring_info(self, idx):
        db = DbConn()
        sql = '''
        select r_name, image_url
        from restaurant
        where r_idx ='''+str(idx)
        rows = db.execute(sql)
        # print(rows)     # [('대학로수제모찌', 'https://store.naver.com/restaurants/detail?id=1205920548')] -> 리스트 안에 튜플 형식 1개 값이 담겨있음
        return rows


    def bring_re(self, idx):
        db = DbConn()
        sql = '''
        select r_idx, user_id, reple, score, rep_time, status
        from restaurant_reple
        where r_idx ='''+str(idx)
        rows = db.execute(sql)
        # print(rows)
        return rows


    def maketable(self, idx):
        self.table = QTableWidget()
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
            
        row = self.bring_re(idx)

        self.table.setColumnCount(6)
        self.table.setRowCount(len(row))

        self.table.setHorizontalHeaderLabels(['가게번호','아이디','리뷰','점수','시간','상태'])
        # self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignRight)
        
        for i in range(len(row)):
            for j in range(len(row[i])):
                self.table.setItem(i,j, QTableWidgetItem(str(row[i][j])))

        self.layout.addWidget(self.table, 2, 0, 1, 2)

