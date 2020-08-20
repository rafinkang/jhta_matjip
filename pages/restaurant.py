import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from classes.DbConn import *

import sys
import cx_Oracle

import math

list_num = 10
db_count = 0

class Restaurant(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.initUI(parent)
        

    def count_restaurant(self):
        sql_count_restaurant = """
        SELECT naver_idx
        FROM restaurant
        """

        db = DbConn()
        db_count_restaurant = db.execute(sql_count_restaurant)
        db_count = len(db_count_restaurant)
        self.page_num = math.ceil(db_count/10)
        print(db_count,self.page_num) 
        
                

    def init_select_restaurant(self):
        sql_select_restaurant = """
        SELECT 
            R_NAME,
            R_CATEGORY,
            PRICE,
            DISTANCE,
            SITE_SCORE,
            SITE_REVIEW,
            MAIN_MENU,
            SITE_REVIEW
        FROM restaurant
        WHERE rownum <= {}
        """.format(list_num)

        # connection = cx_Oracle.connect("scott", "tigertiger", "orcl.czq0cxsnbcns.ap-northeast-2.rds.amazonaws.com"+":1521/orcl")
        # cur = connection.cursor()
        # cur.execute(sql_select_restaurant)
        # db_result_restaurant = cur.fetchall()
        db = DbConn()
        db_result_restaurant = db.execute(sql_select_restaurant)
        print(db_result_restaurant)
        db_exist = len(db_result_restaurant)
        # print(db_exist) 
        
        

        self.label = []
        cnt_row = 0
        for row in db_result_restaurant:
            label_row = []
            cnt_col = 0
            # print("for row 실행중")
            for data in row:
                # print("for data 실행중")
                temp = QLabel(str(data), self)
                label_row.append(temp)
                self.grid.addWidget(temp, cnt_row, cnt_col)
                cnt_col += 1
            cnt_row += 1
            self.label.append(label_row)
                

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

        self.grid = QGridLayout()
        self.setLayout(self.grid)
        
        self.count_restaurant()
        self.init_select_restaurant()
        self.page()
        

        # self.label1 = QLabel("가게이름", self)
        # self.label2 = QLabel("카테고리", self)
        # self.label3 = QLabel("가격", self)
        # self.label4 = QLabel("도보 거리", self)
        # self.label5 = QLabel("네이버 스코어", self)
        # self.label6 = QLabel("사용자 스코어", self)
        # self.label7 = QLabel("네이버 리뷰", self)
        # self.label8 = QLabel("사용자 리뷰", self)
        # self.label9 = QLabel("메뉴", self)
        # self.label10 = QLabel("사이트", self)

