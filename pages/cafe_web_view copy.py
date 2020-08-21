import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import random
import cx_Oracle
from classes.DbConn import *
from PyQt5.QtWebEngineWidgets import QWebEngineView



class CafeWebView(QWidget):
    def __init__(self, parent, url):
        super().__init__(parent)

        self.initUI(url)
        self.form_layout = QBoxLayout(QBoxLayout.LeftToRight, self)
        self.setLayout(self.form_layout)

    def initUI(self,url):
        self.setWindowTitle("QWebEngineView")
        # QWebEngineView 를 이용하여 웹 페이지를 표출
        web = QWebEngineView()
        web.setUrl(QUrl(url))
        self.form_layout.addWidget(web)