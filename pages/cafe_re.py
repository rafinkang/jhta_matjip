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
        # print(idx)
        self.parent = parent
        self.idx = idx
        self.initUI(parent, idx)

    def initUI(self, parent, idx):
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.btn_back = QPushButton("뒤로가기", self)
        # self.layout.addWidget(self.btn_random, 0, 0)
        self.layout.addWidget(self.btn_back, 0, 1)
        self.rilb = QLabel("이미지자리", self)
        self.rnlb = QLabel('식당명', self)
        self.layout.addWidget(self.rilb, 1, 0)
        self.layout.addWidget(self.rnlb, 1, 1)
        self.btn_back.clicked.connect(lambda: parent.route_page('cafe'))
        self.maketable(idx)


    def bring_re(self, idx):
        connection = cx_Oracle.connect('scott','tigertiger','orcl.czq0cxsnbcns.ap-northeast-2.rds.amazonaws.com:1521/orcl')
        # print(connection)
        cur = connection.cursor()
        sql = '''
        select r_idx, user_id, reple, score, rep_time, status
        from restaurant_reple
        where r_idx ='''+str(idx)

        cur.execute(sql)
        rows = cur.fetchall()
        # connection.commit()
        connection.close()
        # print(rows)
        return rows


    def maketable(self, idx):
        self.table = QTableWidget()
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
            
        row = self.bring_re(idx)

        self.table.setColumnCount(7)
        self.table.setRowCount(len(row))

        self.table.setHorizontalHeaderLabels(['가게번호','아이디','리뷰','점수','시간','상태'])
        # self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignRight)
        
        for i in range(len(row)):
            for j in range(len(row[i])):
                self.table.setItem(i,j, QTableWidgetItem(str(row[i][j])))

        self.layout.addWidget(self.table, 2, 0, 1, 2)

