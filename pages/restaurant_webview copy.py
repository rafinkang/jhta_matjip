import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from classes.DbConn import *

import pyautogui

from PyQt5.QtWebEngineWidgets import QWebEngineView


class Restaurant_webview(QWidget):
    def __init__(self, parent, params):
        super().__init__()
        self.parent = parent
        self.params = params
        print(params)
        self.initUI(parent)

        self.select_restaurant_url()

        QWidget.__init__(self, flags=Qt.Widget)
        self.form_layout = QBoxLayout(QBoxLayout.LeftToRight, self)
        self.setLayout(self.form_layout)
        self.init_widget()
        
    def init_widget(self):
        self.setWindowTitle("QWebEngineView")
        # QWebEngineView 를 이용하여 웹 페이지를 표출
        web = QWebEngineView()
        web.setUrl(QUrl(self.url))
        self.form_layout.addWidget(web)

    def select_restaurant_url(self):
        # self.params 를 가지고 셀렉트 돌려서 식당정보 가져오기
        
        sql_select_restaurant_url = """
        SELECT 
            IMAGE_URL
        FROM restaurant
        WHERE r_idx = {}
        """.format(self.params)
            
        db = DbConn()
        self.url = db.execute(sql_select_restaurant_url)[0][0]
        print(self.url)


    def initUI(self, parent):
        self.layout = QGridLayout()
        self.setLayout(self.layout)

# if __name__ == "__main__":
# app = QApplication(sys.argv)
# form = Form()
# form.show()
# exit(app.exec_())