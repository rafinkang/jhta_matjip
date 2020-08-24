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
from pages.mart import *
from pages.mart_basket import *
import urllib.request
from pages.cafe import *
from pages.cafe_re import *

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
            self.setBackgroundImage('images/login.jpg')
            self.setCentralWidget(Login(self))
        elif page_name == 'menu':
            self.setBackgroundImage('images/bg.png')
            self.setCentralWidget(Menu(self))
        elif page_name == 'register':
            self.setBackgroundImage('images/register_type.jpg')
            self.setCentralWidget(Register(self))
        elif page_name == 'find_id':
            self.setBackgroundImage('images/find_id.jpg')
            self.setCentralWidget(FindId(self))
        elif page_name == 'party':
            self.setBackgroundColor('#ffffff')
            self.setCentralWidget(Party(self))
        elif page_name == 'party_insert':
            self.setCentralWidget(PartyInsert(self))
        elif page_name == 'party_detail':
            self.setCentralWidget(PartyDetail(self, params))
        elif page_name == 'restaurant':
            self.setBackgroundColor('#ffffff')
            self.setCentralWidget(Restaurant(self))
        elif page_name == 'restaurant_reple':
            self.setBackgroundColor('#ffffff')
            self.setCentralWidget(Restaurant_reple(self, params))
        elif page_name == 'mart':
            Mart(self)
        elif page_name == 'mart_basket':
            self.setCentralWidget(MartRe(self, params))
        # elif page_name == 'restaurant_webview':
        #     self.setCentralWidget(Restaurant_webview(self, params))
        elif page_name == 'restaurant_webview':
            self.setCentralWidget(Restaurant_webview(self, params))
        elif page_name == 'cafe':
            self.setBackgroundColor('#ffffff')
            self.setCentralWidget(Cafe(self))
        elif page_name == 'cafe_re':
            self.setBackgroundColor('#ffffff')
            self.setCentralWidget(CafeRe(self, params))
        # elif page_name == 'cafe_web_view':
        #     self.cwv = self.CafeWebView(self)
        
        # elif page_name == '':
        #     self.setCentralWidget(Class(self))
        
    def setBackgroundImage(self, url, web = False):
        if web:
            imageFromWeb = urllib.request.urlopen(url).read()
            q_img = QPixmap()
            q_img.loadFromData(imageFromWeb)
        else:
            q_img = QPixmap(url)
        s_img = q_img.scaled(QSize(self.width(), self.height()))
        palette = QPalette()
        palette.setBrush(10, QBrush(s_img))
        self.setPalette(palette)
    
    def setBackgroundColor(self, color):
        palette = QPalette()
        palette.setColor(self.backgroundRole(), QColor(color))
        self.setPalette(palette)
    


if __name__ == "__main__":  
    app = QApplication(sys.argv)
    main = JhtaMatjip()
    
    # 첫 화면 실행
    main.route_page('login')
    sys.exit(app.exec_())