import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
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
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.img = QPixmap('https://search.pstatic.net/common/?autoRotate=true&type=w560_sharpen&src=http%3A%2F%2Fldb.phinf.naver.net%2F20200414_82%2F1586848471077L0cmi_JPEG%2Fa7vlVmTCgJhJ2JNsUEPL-t8m.jpg')
        self.layout.addWidget(self.img,0,0)
        self.btn_back = QPushButton("뒤로가기", self)
        self.layout.addWidget(self.btn_back, 0, 2)
        self.btn_back.clicked.connect(lambda: parent.route_page('cafe'))
        datas = self.bring_info(self.idx)
        self.data = datas[0]

        self.rnlb = QLabel(self.data[0], self)       # 리스트 0번째 튜플의 0번째 것
        self.btn_site = QPushButton("사이트 바로 가기", self)
        self.layout.addWidget(self.rnlb, 1, 0, 1, 2)
        self.layout.addWidget(self.btn_site, 1, 2)
        # print(self.data[1])
        self.btn_site.clicked.connect(lambda: self.new_window(self.data[1]))

        self.combo = QComboBox()
        for i in range(11):
            self.combo.addItem(str(5-i*0.5)+'점')
        self.ed_reple = QLineEdit()
        self.btn_reple = QPushButton('댓글 달기', self)
        self.layout.addWidget(self.combo, 2, 0)
        self.layout.addWidget(self.ed_reple, 2, 1)
        self.layout.addWidget(self.btn_reple, 2, 2)
        self.btn_reple.clicked.connect(self.reple)

        self.maketable(idx)


    def bring_info(self, idx):
        db = DbConn()
        sql = '''
        select r_name, image_url
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
            rep_time = time.ctime()
            db = DbConn()
            db.execute(sql,
                {'r_idx':self.idx,
                'user_id':self.parent.user_id,
                'reple':text,
                'score':score,})
        self.parent.route_page('cafe_re', self.idx)


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