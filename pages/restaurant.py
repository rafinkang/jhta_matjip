import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from classes.DbConn import *

import sys
import cx_Oracle

import math
import random
import pyautogui

class Restaurant(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.list_num = 300
        self.list_count = 1
        self.db_count = 0
        self.initUI(parent)
        

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
        self.btn_random_restaurant = QPushButton("랜덤", self)
        self.btn_back = QPushButton("뒤로가기", self)
        self.layout.addWidget(self.btn_random_restaurant, 0 ,0)
        self.layout.addWidget(self.btn_back, 0, 1)

        # self.count_restaurant_table()
        self.create_restaurant_table()
        
        self.btn_random_restaurant.clicked.connect(self.random_restaurant)
        self.btn_back.clicked.connect(lambda: parent.route_page('menu'))
        
    def random_restaurant(self):
        rand = random.randint(1,self.list_num)
        rand_restaurant = self.db_result_restaurant[rand][0]
        rand_restaurant_cate = self.db_result_restaurant[rand][1]
        rand_restaurant_menu = self.db_result_restaurant[rand][8]
        pyautogui.alert("오늘은 '{}' 가보는건 어떨까요?\n{} 가게 입니다.\n{} !!!".format(rand_restaurant,rand_restaurant_cate,rand_restaurant_menu))


    def create_restaurant_table(self):
        
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
        WHERE R_CATEGORY not like '%카페%'
        """

        db = DbConn()
        self.db_result_restaurant = db.execute(sql_select_restaurant)
        # print(self.db_result_restaurant)
        self.list_num = len(self.db_result_restaurant)

        self.table = QTableWidget()        
        
        # self.table.setSelectionBehavior(QTableView.SelectRows) # multiple row 선택 가능 
        self.table.setSelectionMode(QAbstractItemView.SingleSelection) 
        
        # row, column 갯수 설정해야만 tablewidget 사용할수있다. 
        self.table.setColumnCount(9) 
        self.table.setRowCount(self.list_num) 
        # column header 명 설정. 
        self.table.setHorizontalHeaderLabels(["식당", "카테고리", "가격", "거리", "평점", "네이버 점수", "리뷰수", "네이버 리뷰수", "대표메뉴"]) 
        

        row_num = 0
        for row in self.db_result_restaurant:
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