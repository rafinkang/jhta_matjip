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
        self.parent = parent
        self.list_num = 300
        self.list_count = 1
        self.db_count = 0
        self.btn_restaurant_reple = []
        self.initUI(parent)
        


    def initUI(self, parent):
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.btn_random_restaurant = QPushButton("", self)
        self.btn_back = QPushButton("", self)
        
        icon_back  = QIcon('images/back.png')
        self.btn_back.setIcon(icon_back)
        self.btn_back.resize(50, 50)
        self.btn_back.setIconSize(QSize(50, 50))
        self.btn_back.setStyleSheet('background-color: transparent')

        icon_random_restaurant  = QIcon('images/random.png')
        self.btn_random_restaurant.setIcon(icon_random_restaurant)
        self.btn_random_restaurant.resize(50, 50)
        self.btn_random_restaurant.setIconSize(QSize(50, 50))
        self.btn_random_restaurant.setStyleSheet('background-color: transparent')

        hbox = QHBoxLayout()
        hbox.addStretch()

        pixmap_ori = QPixmap('images/ori.png')
        pixmap_ori = pixmap_ori.scaledToWidth(50)
        pixmap_ori = pixmap_ori.scaledToHeight(50)
        label_ori = QLabel()
        label_ori.setPixmap(pixmap_ori)
        
        # label_size = QLabel(Width: 50, Height: 50)
        # lbl_size.setAlignment(Qt.AlignCenter)

        hbox.addWidget(label_ori)
        
        hbox.addWidget(self.btn_back)
        self.layout.addLayout(hbox,0,1)

        self.layout.addWidget(self.btn_random_restaurant, 0 ,0)
        # self.layout.addWidget(self.btn_back, 0, 1)

        self.create_restaurant_table()
        
        self.btn_random_restaurant.clicked.connect(self.random_restaurant)
        self.btn_back.clicked.connect(lambda: parent.route_page('menu'))
        # for i in range(len(self.btn_restaurant_reple)):
        #     # self.btn_restaurant_reple[i].clicked.connect(lambda: parent.route_page('restaurant_reple', self.restaurant_idx[i]))
        #     self.btn_restaurant_reple[i].clicked.connect(lambda: print(self.restaurant_idx[i],i,"번째것 클릭되었습니다."))
        for btn, index in self.btn_restaurant_reple:
            # print(btn, index)
            self.connect_btn(btn, index)
            

        # print(self.restaurant_idx)
    def connect_btn(self, btn, index):
        btn.clicked.connect(lambda: self.parent.route_page('restaurant_reple',index))
        
    def random_restaurant(self):
        rand = random.randint(1,self.list_num)
        rand_restaurant = self.db_result_restaurant[rand][0]
        rand_restaurant_cate = self.db_result_restaurant[rand][1]
        rand_restaurant_menu = self.db_result_restaurant[rand][8]
        pyautogui.alert("오늘은 '{}' 가보는건 어떨까요?\n{} 가게 입니다.\n{} !!!".format(rand_restaurant,rand_restaurant_cate,rand_restaurant_menu))


    def create_restaurant_table(self):
        self.restaurant_idx = []

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
            MAIN_MENU,
            R_IDX
        FROM restaurant
        WHERE R_CATEGORY not like '%카페%'
        ORDER BY r_idx ASC
        """

        db = DbConn()
        self.db_result_restaurant = db.execute(sql_select_restaurant)
        # print(self.db_result_restaurant)
        self.list_num = len(self.db_result_restaurant)

        self.table = QTableWidget()        
        
        # self.table.setSelectionBehavior(QTableView.SelectRows) # multiple row 선택 가능 
        self.table.setSelectionMode(QAbstractItemView.SingleSelection) 
        
        # row, column 갯수 설정해야만 tablewidget 사용할수있다. 
        self.table.setColumnCount(10) 
        self.table.setRowCount(self.list_num) 
        # column header 명 설정. 
        self.table.setHorizontalHeaderLabels(["식당", "카테고리", "가격", "거리", "평점", "네이버 점수", "리뷰수", "네이버 리뷰수", "대표메뉴", "리뷰확인"]) 
        

        row_num = 0
        for row in self.db_result_restaurant:
            col_num = 0
            for data in row:
                if col_num == 9:
                    # 글씨 쓰는게 아니라 버튼만 설치
                    item_widget = QPushButton("리뷰확인") 
                    self.btn_restaurant_reple.append([item_widget, data])
                    self.table.setCellWidget(row_num, col_num, item_widget) 
                    self.restaurant_idx.append(data)
                else:
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
        self.table.setColumnWidth(8, 150) #컬럼 사이즈 설정
        self.table.setColumnWidth(9, 60) #컬럼 사이즈 설정
        
        self.layout.addWidget(self.table, 1, 0, 1,2)