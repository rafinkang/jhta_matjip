import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import random
import cx_Oracle
from classes.DbConn import *
from PyQt5.QtWebEngineWidgets import QWebEngineView



class CafeWebView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowTitle("QWebEngineView")
        self.show()


    def initUI(self, parent, url):
        self.setCentralWidget(web(self))

    
class Site(QWidget):
    def __init__(self, parent, url):
        super().__init__(parent)
        self.layout = QBoxLayout(QBoxLayout.LeftToRight, self)
        self.setLayout(self.form_layout)
        web = QWebEngineView()
        web.setUrl(QUrl(url))
        self.layout.addWidget(web)
