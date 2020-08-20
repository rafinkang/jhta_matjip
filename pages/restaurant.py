import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from classes.DbConn import *

import sys
import cx_Oracle

import math


class Restaurant(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.list_num = 17
        self.list_count = 1
        self.db_count = 0
        self.initUI(parent)
        

    def count_restaurant(self):
        sql_count_restaurant = """
        SELECT naver_idx
        FROM restaurant
        """

        db = DbConn()
        db_count_restaurant = db.execute(sql_count_restaurant)
        self.db_count = len(db_count_restaurant)
        self.page_num = math.ceil(self.db_count/10)
        print(self.db_count,self.page_num) 
        
                

    def page(self):
        
        self.label_page = []
        cnt_row = 0
        cnt_col = 0
        for i in range(self.page_num):
            temp = QPushButton(str(i+1), self)
            self.label_page.append(temp)
            self.grid.addWidget(temp, 10, cnt_col)
            cnt_col += 1
            # print("실행중")
            temp.clicked.connect(lambda: print("임시{}".format(str(i))))

    def initUI(self, parent):
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.btn_addmore = QPushButton("더보기", self)
        self.btn_back = QPushButton("뒤로가기", self)
        self.layout.addWidget(self.btn_addmore, 0, 0)
        self.layout.addWidget(self.btn_back, 0, 1)
        self.create_restaurant_table()
        
        self.btn_back.clicked.connect(lambda: parent.route_page('menu'))
        self.btn_addmore.clicked.connect(self.addmore_restaurant)

    def addmore_restaurant(self):
        
        sql_select_restaurant = """
        SELECT 
            R_NAME,
            R_CATEGORY,
            PRICE,
            DISTANCE,
            SCORE,
            SITE_SCORE,
            REVIEW,
            SITE_REVIEW,
            MAIN_MENU
        FROM restaurant
        WHERE rownum BETWEEN {} and  {}
        """.format(self.list_num*self.list_count, self.list_num*(self.list_count+1))
        print(sql_select_restaurant)
        self.list_count += 1

        db = DbConn()
        db_result_restaurant = db.execute(sql_select_restaurant)
        print(db_result_restaurant)
        db_exist = len(db_result_restaurant)





    def create_restaurant_table(self):
        self.table = QTableWidget()        
        
        # self.table.setSelectionBehavior(QTableView.SelectRows) # multiple row 선택 가능 
        self.table.setSelectionMode(QAbstractItemView.SingleSelection) 
        
        # row, column 갯수 설정해야만 tablewidget 사용할수있다. 
        self.table.setColumnCount(9) 
        self.table.setRowCount(self.list_num) 
        # column header 명 설정. 
        self.table.setHorizontalHeaderLabels(["식당", "카테고리", "가격", "거리", "평점", "네이버 점수", "리뷰수", "네이버 리뷰수", "대표메뉴"]) 
        
        sql_select_restaurant = """
        SELECT 
            R_NAME,
            R_CATEGORY,
            PRICE,
            DISTANCE,
            SCORE,
            SITE_SCORE,
            REVIEW,
            SITE_REVIEW,
            MAIN_MENU
        FROM restaurant
        WHERE rownum <= {}
        """.format(self.list_num)

        db = DbConn()
        db_result_restaurant = db.execute(sql_select_restaurant)
        # print(db_result_restaurant)
        db_exist = len(db_result_restaurant)

        row_num = 0
        for row in db_result_restaurant:
            col_num = 0
            for data in row:
                self.table.setItem(row_num, col_num, QTableWidgetItem(str(data))) 
                col_num += 1
            row_num += 1
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) # edit 금지 모드 
        self.table.setColumnWidth(2, 70) #컬럼 사이즈 설정
        self.table.setColumnWidth(3, 50) #컬럼 사이즈 설정
        self.table.setColumnWidth(4, 50) #컬럼 사이즈 설정
        self.table.setColumnWidth(5, 50) #컬럼 사이즈 설정
        self.table.setColumnWidth(6, 50) #컬럼 사이즈 설정
        self.table.setColumnWidth(7, 50) #컬럼 사이즈 설정
        self.table.setColumnWidth(8, 200) #컬럼 사이즈 설정
        
        self.layout.addWidget(self.table, 1, 0, 1,2)