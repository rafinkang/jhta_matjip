import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap
import urllib.request

import random
import cx_Oracle
from classes.DbConn import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
import pyautogui
import time



class CafeRe(QWidget):
    def __init__(self, parent, idx):
        super().__init__(parent)
        # print(idx)
        self.parent = parent       # 각 함수에서 필요한 매개변수를 지정했으므로 전역변수화 필요 없음       
        self.idx = idx         # -> self.로 전역변수 처리하면 각 함수에 매개변수 지정 안 해도 됨
        self.initUI(parent,idx)


    def initUI(self, parent, idx):
        datas = self.bring_info(self.idx)
        self.data = datas[0]

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.img_lb = QLabel()
        if self.data[2] != '없음':
            url = self.data[2]
            self.img = urllib.request.urlopen(url).read()   
            self.pixmap = QPixmap()
            self.pixmap.loadFromData(self.img)
            self.img_lb.setPixmap(self.pixmap)
        else :
            pass
        self.layout.addWidget(self.img_lb, 0, 0)

        # self.btn_back = QPushButton("뒤로가기", self)

        self.btn_back = QPushButton("", self)
        icon_back = QIcon('images/back.jpg')
        self.btn_back.setIcon(icon_back)     
        self.btn_back.resize(133,133)
        self.btn_back.setIconSize(QSize(70,70))
        self.btn_back.setStyleSheet('background-color: transparent')
        self.layout.addWidget(self.btn_back, 0, 2)
        self.btn_back.clicked.connect(lambda: parent.route_page('cafe'))

        self.rnlb = QLabel(self.data[0], self)       # 리스트 0번째 튜플의 0번째 것
        self.btn_site = QPushButton("사이트 보기", self)
        self.btn_site.setStyleSheet('background-color: #FFD93A;'
                                    'padding: 10px;'
                                    'font: bold 11px;'
                                    'border: 2px solid orange;'
                                    'border-radius: 10px;')
        self.layout.addWidget(self.rnlb, 1, 0, 1, 2)
        self.layout.addWidget(self.btn_site, 1, 2)
        # print(self.data[1])
        self.btn_site.clicked.connect(lambda: self.new_window('https://store.naver.com/restaurants/detail?entry=pll&id='+str(self.data[1])))

        self.combo = QComboBox()
        for i in range(11):
            self.combo.addItem(str(5-i*0.5)+'점')
        self.ed_reple = QLineEdit()
        self.btn_reple = QPushButton('댓글 달기', self)
        self.btn_reple.setStyleSheet('background-color: #FFD93A;'
                                    'padding: 10px;'
                                    'font: bold 11px;'
                                    'border: 2px solid orange;'
                                    'border-radius: 10px;')
        self.layout.addWidget(self.combo, 2, 0)
        self.layout.addWidget(self.ed_reple, 2, 1)
        self.layout.addWidget(self.btn_reple, 2, 2)
        self.btn_reple.clicked.connect(self.reple)

        self.maketable(idx)


    def bring_info(self, idx):
        db = DbConn()
        sql = '''
        select r_name, naver_idx, image_url
        from restaurant
        where r_idx ='''+str(idx)
        rows = db.execute(sql)
        # print(rows[0][1])     # [('대학로수제모찌', 'https://store.naver.com/restaurants/detail?id=1205920548')] -> 리스트 안에 튜플 형식 1개 값이 담겨있음
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
                
        self.table.setColumnWidth(0, 70) #컬럼 사이즈 설정        
        self.table.setColumnWidth(2, 300) #컬럼 사이즈 설정        
        self.table.setColumnWidth(3, 70) #컬럼 사이즈 설정        
        self.table.setColumnWidth(4, 150) #컬럼 사이즈 설정        
        self.table.setColumnWidth(5, 70) #컬럼 사이즈 설정        

        self.layout.addWidget(self.table, 3, 0, 1, 3)


    def new_window(self, url):        # 버튼 클릭하면 새창 띄우는 이벤트 핸들러
        self.nw = CafeWebView(self, url)         # 새로운 윈도우 객체
        self.nw.show()

    
    def reple(self):         # 댓글 달기 버튼 누르면 실행하는 함수
        text = self.ed_reple.text()
        if len(text) == 0:
            pyautogui.alert('뭘 먹었는지, 맛은 어땠는지 내용을 남기렴..')
        else:
            score = float(self.combo.currentText()[:3])     
            # print(score)
            self.ed_reple.setText('')       # 댓글 달리면 댓글창 내용 리셋

            sql = '''
            INSERT INTO restaurant_reple(
                r_idx,
                user_id,
                reple,
                score,
                rep_time
            ) VALUES(
                :r_idx,
                :user_id,
                :reple,
                :score,
                sysdate
            )
            '''
            # rep_time = time.ctime()
            db = DbConn()
            db.execute(sql,
                {'r_idx':self.idx,
                'user_id':self.parent.user_id,
                'reple':text,
                'score':score,})
            self.refresh_user_score()
            self.parent.route_page('cafe_re', self.idx)


    def refresh_user_score(self):
        sql_select_score = """
            SELECT 
                score
            FROM
                restaurant_reple
            WHERE
                r_idx = :r_idx
            """
        
        db = DbConn()
        self.score_list = db.execute(sql_select_score,
                            {'r_idx': self.idx})
        self.review_num = len(self.score_list)
        total_score = 0
        for score in self.score_list:
            total_score += score[0]
        avg_score = round(total_score/self.review_num, 2)
        # print(avg_score)

    # db에 입력하기
        sql_update_score = """
        UPDATE restaurant SET
            score = :score,
            review = :review
        WHERE r_idx = :r_idx
        """

        db = DbConn()
        self.score_list = db.execute(sql_update_score,
                            {'score': avg_score,
                             'review': self.review_num,
                             'r_idx': self.idx})    

class CafeWebView(QMainWindow):
    def __init__(self, parent, url):
        super().__init__(parent)
        self.setCentralWidget(Site(self, url))
        self.setWindowTitle("QWebEngineView")
        self.show()


class Site(QWidget):
    def __init__(self, parent, url):
        super().__init__(parent)
        self.initUI(parent, url)


    def initUI(self, parent, url):
        self.layout = QBoxLayout(QBoxLayout.LeftToRight, self)
        self.setLayout(self.layout)
        web = QWebEngineView()
        web.setUrl(QUrl(url))
        self.layout.addWidget(web)