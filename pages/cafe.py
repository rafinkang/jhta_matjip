import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import random
import cx_Oracle
from classes.DbConn import *


class Cafe(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.initUI(parent)


    def initUI(self, parent):
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.btn_random = QPushButton("랜덤뽑기 ㅋ", self)
        self.btn_back = QPushButton("뒤로가기", self)
        self.layout.addWidget(self.btn_random, 0, 0)
        self.layout.addWidget(self.btn_back, 0, 1)
        self.maketable()
        self.btn_random.clicked.connect(self.random)
        self.btn_back.clicked.connect(lambda: parent.route_page('menu'))


    def bringdata(self):
        connection = cx_Oracle.connect('scott','tigertiger','orcl.c2yvx9kfplxi.ap-northeast-2.rds.amazonaws.com:1521/orcl')
        # print(connection)
        cur = connection.cursor()
        sql = '''
        select r_name, site_score, site_review, distance, r_category, price, review 
        from restaurant
        '''
        cur.execute(sql)
        rows = cur.fetchall()
        # connection.commit()
        connection.close()
        # print(rows)
        return rows


    def random(self):
        row = self.bringdata()
        self.btn_random.setText(row[random.randint(0,len(row))][0])
        QMessageBox.question(self,'결과는 두구두구두구',row[random.randint(0,len(row))][0]+'/n가즈아',QMessageBox.Yes)

    def maketable(self):
        self.table = QTableWidget()
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
            
        row = self.bringdata()

        self.table.setColumnCount(7)
        self.table.setRowCount(len(row))

        self.table.setHorizontalHeaderLabels(['가게명','네이버평점','네이버리뷰수','거리','카테고리','가격','jhta리뷰'])
        # self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignRight)
        
        for i in range(len(row)):
            for j in range(len(row[i])):
                self.table.setItem(i,j, QTableWidgetItem(str(row[i][j])))

        self.layout.addWidget(self.table, 1, 0, 1, 2)

