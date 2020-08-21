import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cx_Oracle
from classes.DbConn import *



class MartRe(QWidget):
    def __init__(self, parent, idx):
        super().__init__(parent)
        # print(idx)
        # self.parent = parent       # 각 함수에서 필요한 매개변수를 지정했으므로 전역변수화 필요 없음       
        self.idx = idx         # -> self.로 전역변수 처리하면 각 함수에 매개변수 지정 안 해도 됨
        # self.initUI(parent, idx)
        self.maketable(idx)


    def bring_re(self, idx):
        pass

    def maketable(self, idx):
        self.table = QTableWidget()
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
            
        row = self.bring_re(idx)

        self.table.setColumnCount(7)
        self.table.setRowCount(len(row))

        self.table.setHorizontalHeaderLabels(['가게번호','아이디','리뷰','점수','시간','상태'])
        # self.table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignRight)
        
        for i in range(len(row)):
            for j in range(len(row[i])-1):
                self.table.setItem(i,j, QTableWidgetItem(str(row[i][j+1])))

        self.layout.addWidget(self.table, 2, 0, 1, 2)