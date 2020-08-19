from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
from pathlib import Path
from selenium import webdriver
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui


db = DbConn("orcl.c2yvx9kfplxi.ap-northeast-2.rds.amazonaws.com")
print(db.execute("select * from dept"))


# 카페 네이버id 뽑아오기  
url = 'https://store.naver.com/restaurants/list?entry=pll&filterId=r09110133&menu=1&query=%EC%9D%B5%EC%84%A0%EB%8F%99%20%EB%A7%9B%EC%A7%91&sessionid=7veS51p6yK7aLxRRrqMRQg%3D%3D'
res = requests.get(url)
res.raise_for_status()      # 만약 에러가 있으면 에러 메세지 출력 후 끝내고 아니면 하위에 코드를 실행
soup = bs(res.text,'lxml')
p = re.compile('"id":"[0-9]+","name":"[가-힣]+"')
stores = p.findall(str(soup))
id = []
for store in stores:
    id.append(store.split(',')[0][6:-1])
# print(len(id))


# 카페 네이버 id로 각 상세 페이지에 접속
url = 'https://store.naver.com/restaurants/detail?entry=pll&id='
browser = webdriver.Chrome('e:/dev/python_workspace/chromedriver.exe')


info = []
# 정보 뽑아오기  
for j in range(len(id)):
    try:
        browser.get(url+id[j])
        browser.maximize_window()
        time.sleep(1)
        # for i in range(1,21):
        storeElem = browser.find_element_by_css_selector('#content > div:nth-child(1) > div.biz_name_area > strong')
        store = storeElem.text
        # print(store)
        menuElem = browser.find_element_by_css_selector('#content > div:nth-child(2) > div.bizinfo_area > div > div.list_item.list_item_menu > div > ul > li:nth-child(1) > div > div > div > span.name')
        menu = menuElem.text
        # print(menu)
        priceElem = browser.find_element_by_css_selector('#content > div:nth-child(2) > div.bizinfo_area > div > div.list_item.list_item_menu > div > ul > li:nth-child(1) > div > em')       
        price = priceElem.text
        disElem = brower.
        distance = 

        nreviewElem = browser.find_element_by_class_name('count')       
        nreview = nreviewElem.text
        # print(j,'https://store.naver.com/restaurants/detail?id='+str(j),store, menu, price, nreview)
        dic = dict(naver_idx=j, r_name=store, r_category='카페',price=price, image_url='https://store.naver.com/restaurants/detail?id='+str(id[j]), distance=None, score=None, site_score=None, review=None, site_reivew=nreview, main_menu=menu)
        print(dic)
        # info.append({store,menu,price,nreview})
    except Exception as e:
        if e == 'Message: no such element: Unable to locate element: {"method":"css selector","selector":"#content > div:nth-child(2) > div.bizinfo_area > div > div.list_item.list_item_menu > div > ul > li:nth-child(1) > div > div > div > span.name"}':
            menu = ''
        if e == 'Message: no such element: Unable to locate element: {"method":"css selector","selector":".count"}':
            nreview is None

# print('--------------------------------')

# time.sleep(2)