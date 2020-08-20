import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import random
import cx_Oracle
from classes.DbConn import *


class CafeRe(QWidget):
    def __init__(self, parent, idx):
        super().__init__(parent)
        print(idx)
        self.initUI(parent, idx)

    def initUI(self, parent, idx):
        self.idx = idx
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.rilb = QLabel("이미지자리", self)
        self.rnlb = QLabel('식당명', self)
        self.layout.addWidget(self.btn_random, 0, 0)
        self.layout.addWidget(self.btn_back, 0, 1)


    def bring_re(self):
        connection = cx_Oracle.conne,ct('scott','tigertiger','orcl.czq0cxsnbcns.ap-northeast-2.rds.amazonaws.com:1521/orcl')
        # print(connection)
        cur = connection.cursor()
        sql = '''
        select mr_idx, user_id, rep_time, score, reple
        from menu_reple
        '''
        cur.execute(sql)
        rows = cur.fetchall()
        # connection.commit()
        connection.close()
        # print(rows)
        return rows


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

