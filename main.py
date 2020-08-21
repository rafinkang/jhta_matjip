import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from classes.DbConn import *
# import pages 
from pages.login import *
from pages.menu import *
from pages.register import *
from pages.find_id import *
from pages.party import *
from pages.party_insert import *
from pages.party_detail import *
from pages.restaurant import *
from pages.restaurant_reple import *
# from pages.mart import *
from pages.cafe import *
from pages.cafe_re import *
from pages.cafe_web_view import *

# pip install PyQtWebEngine
# 실행해서 설치해주세요


class JhtaMatjip(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JhtaMatjip")
        self.setGeometry(100, 100, 800, 600)
        self.show()
        
        
    def route_page(self, page_name, params = None):
        if page_name == 'login':
            self.setCentralWidget(Login(self))
        elif page_name == 'menu':
            self.setCentralWidget(Menu(self))
        elif page_name == 'register':
            self.setCentralWidget(Register(self))
        elif page_name == 'find_id':
            self.setCentralWidget(FindId(self))
        elif page_name == 'party':
            self.setCentralWidget(Party(self))
        elif page_name == 'party_insert':
            self.setCentralWidget(PartyInsert(self))
        elif page_name == 'party_detail':
            self.setCentralWidget(PartyDetail(self, params))
        elif page_name == 'restaurant':
            self.setCentralWidget(Restaurant(self))
        # elif page_name == 'mart':
        #     self.setCentralWidget(Mart(self))
        elif page_name == 'restaurant_reple':
            self.setCentralWidget(Restaurant_reple(self, params))
        elif page_name == 'restaurant_webview':
            self.setCentralWidget(Restaurant_webview(self, params))
        elif page_name == 'cafe':
            self.setCentralWidget(Cafe(self))
        elif page_name == 'cafe_re':
            self.setCentralWidget(CafeRe(self, params))
        # elif page_name == 'cafe_web_view':
        #     self.cwv = self.CafeWebView(self)
        
        # elif page_name == '':
        #     self.setCentralWidget(Class(self))


if __name__ == "__main__":  
    app = QApplication(sys.argv)
    main = JhtaMatjip()
    
    # 첫 화면 실행
    main.route_page('login')
    sys.exit(app.exec_())