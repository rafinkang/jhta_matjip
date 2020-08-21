import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from classes.DbConn import *


class Restaurant_reple(QWidget):
    def __init__(self, parent, params):
        super().__init__()
        self.parent = parent
        self.params = params
        print(params)
        self.initUI(parent)
        
    def select_restaurant(self):
        # self.params 를 가지고 셀렉트 돌려서 식당정보 가져오기
        
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
        WHERE r_idx = {}
        """.format(self.params)
        # print(sql_select_restaurant)
        
        db = DbConn()
        self.db_result_restaurant = db.execute(sql_select_restaurant)
        # print(self.db_result_restaurant, "이거 확인")
        # self.list_num = len(self.db_result_restaurant)
        
        
        sql_select_restaurant_reple = """
        SELECT 
            rep_time,
            user_id,
            score,
            reple
        FROM restaurant_reple
        WHERE r_idx = {}
        """.format(self.params)
        # print(sql_select_restaurant)
        
        db = DbConn()
        self.db_result_restaurant_reple = db.execute(sql_select_restaurant_reple)
        # print(self.db_result_restaurant_reple, "이거 확인")
        # self.list_num = len(self.db_result_restaurant)




    def initUI(self, parent):
        self.select_restaurant()

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.label_restaurant_name1 = QLabel("식당이름",self)
        self.label_restaurant_category1 = QLabel("카테고리",self)
        self.label_restaurant_price1 = QLabel("가격",self)
        self.label_restaurant_distance1 = QLabel("거리",self)
        self.label_restaurant_score1 = QLabel("평점",self)
        self.label_restaurant_nscore1 = QLabel("네이버점수",self)
        self.label_restaurant_review1 = QLabel("리뷰수",self)
        self.label_restaurant_nreview1 = QLabel("네이버리뷰수",self)
        self.label_restaurant_menu1 = QLabel("대표메뉴",self)

        self.label_restaurant_name2 = QLabel(self.db_result_restaurant[0][0],self)
        self.label_restaurant_category2 = QLabel(self.db_result_restaurant[0][1],self)
        self.label_restaurant_price2 = QLabel(str(self.db_result_restaurant[0][2]),self)
        self.label_restaurant_distance2 = QLabel(self.db_result_restaurant[0][3],self)
        self.label_restaurant_score2 = QLabel(str(self.db_result_restaurant[0][4]),self)
        self.label_restaurant_nscore2 = QLabel(str(self.db_result_restaurant[0][5]),self)
        self.label_restaurant_review2 = QLabel(str(self.db_result_restaurant[0][6]),self)
        self.label_restaurant_nreview2 = QLabel(str(self.db_result_restaurant[0][7]),self)
        self.label_restaurant_menu2 = QLabel(self.db_result_restaurant[0][8],self)

        self.layout.addWidget(self.label_restaurant_name1, 0, 0)
        self.layout.addWidget(self.label_restaurant_category1, 0, 1)
        self.layout.addWidget(self.label_restaurant_price1, 0, 2)
        self.layout.addWidget(self.label_restaurant_distance1, 0, 3)
        self.layout.addWidget(self.label_restaurant_score1, 0, 4)
        self.layout.addWidget(self.label_restaurant_nscore1, 0, 5)
        self.layout.addWidget(self.label_restaurant_review1, 0, 6)
        self.layout.addWidget(self.label_restaurant_nreview1, 0, 7)
        self.layout.addWidget(self.label_restaurant_menu1, 0, 8)

        self.layout.addWidget(self.label_restaurant_name2, 1, 0)
        self.layout.addWidget(self.label_restaurant_category2, 1, 1)
        self.layout.addWidget(self.label_restaurant_price2, 1, 2)
        self.layout.addWidget(self.label_restaurant_distance2, 1, 3)
        self.layout.addWidget(self.label_restaurant_score2, 1, 4)
        self.layout.addWidget(self.label_restaurant_nscore2, 1, 5)
        self.layout.addWidget(self.label_restaurant_review2, 1, 6)
        self.layout.addWidget(self.label_restaurant_nreview2, 1, 7)
        self.layout.addWidget(self.label_restaurant_menu2, 1, 8)
        
        self.combobox_score = QComboBox()
        self.lineedit_reple = QLineEdit()

        self.layout.addWidget(self.combobox_score, 2, 0, 1, 1)
        self.layout.addWidget(self.lineedit_reple, 2, 1, 1, 8)

        for i in range(11):
            self.combobox_score.addItem(str(5-i*0.5)+"점")
        
        

        # self.btn_new_party = QPushButton("파티생성", self)
        self.btn_back = QPushButton("뒤로가기", self)
        # self.layout.addWidget(self.btn_new_party, 0, 0)
        self.layout.addWidget(self.btn_back, 0, 9, 2, 1)
        self.create_table()
        
        self.btn_back.clicked.connect(lambda: parent.route_page('restaurant'))
    
    def create_table(self):
        self.table = QTableWidget()        
        
        # self.table.setSelectionBehavior(QTableView.SelectRows) # multiple row 선택 가능 
        self.table.setSelectionMode(QAbstractItemView.SingleSelection) 
        
        # row, column 갯수 설정해야만 tablewidget 사용할수있다. 
        self.table.setColumnCount(4) 
        self.table.setRowCount(16) 
        # column header 명 설정. 
        self.table.setHorizontalHeaderLabels(["날짜", "아이디", "평점", "먹은음식 및 평가"]) 
        
        row_num = 0
        for row in self.db_result_restaurant_reple:
            col_num = 0
            for data in row:
                self.table.setItem(row_num, col_num, QTableWidgetItem(str(data))) 
                # print(str(data))
                col_num += 1
            row_num += 1
        
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers) # edit 금지 모드 
        self.table.setColumnWidth(0, 150) #컬럼 사이즈 설정
        self.table.setColumnWidth(1, 100) #컬럼 사이즈 설정
        self.table.setColumnWidth(2, 50) #컬럼 사이즈 설정
        self.table.setColumnWidth(3, 450) #컬럼 사이즈 설정
        

        self.layout.addWidget(self.table, 3, 0, 1,10)