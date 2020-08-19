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

import cx_Oracle


# 카페 네이버id 뽑아오기  
url = 'https://store.naver.com/restaurants/list?entry=pll&filterId=r09110133&menu=1&query=%EC%9D%B5%EC%84%A0%EB%8F%99%20%EB%A7%9B%EC%A7%91&sessionid=7veS51p6yK7aLxRRrqMRQg%3D%3D'
res = requests.get(url)
res.raise_for_status()      # 만약 에러가 있으면 에러 메세지 출력 후 끝내고 아니면 하위에 코드를 실행
soup = bs(res.text,'lxml')
p = re.compile('"id":"[0-9]+","name":"[가-힣]+"')
stores = p.findall(str(soup))
id = []      # 62개 -> 42개
for store in stores:
    if store.split(',')[0][6:-1] not in ['1779964403', '1105473067', '1476550727', '939051630', '1647032458', '11715731', '1141273055', '1006047375', '636720810', '1764065667', '34582227', '34850621', '731605639', '1669479895', '1584325830', '1804950881', '1507052049', '1386833963', '1614417324', '1250997417']:
        id.append(store.split(',')[0][6:-1])
# print(len(id))


# # 카페 네이버 id로 각 상세 페이지에 접속
url = 'https://store.naver.com/restaurants/detail?entry=pll&id='
browser = webdriver.Chrome('e:/dev/python_workspace/chromedriver.exe')

browser.get(url+id[0])
disElem = browser.find_element_by_css_selector('#panel01 > div > div.sc_box.contact > div.contact_area > div > div > ul:nth-child(2) > li:nth-child(1) > div:nth-child(2) > div > span > span > span.info > em')
print(disElem.text)

# 정보 뽑아오기  
for j in range(len(id)):
    try: 
        browser.get(url+id[j])
        time.sleep(1)

        storeElem = browser.find_element_by_css_selector('#content > div:nth-child(1) > div.biz_name_area > strong')
        store = storeElem.text
    # print(store)

        print(count, store, browser.find_element_by_css_selector('#panel01 > div > div.sc_box.contact > div.contact_area > div > div > ul:nth-child(2)').text[4:10])
        print('-----------------------------')
        #     disElem = browser.find_element_by_css_selector('#panel01 > div > div.sc_box.contact > div.contact_area > div.txt > div > span')
        # print(disElem.text)
        # p = re.compile('도보 [0-9]분')
        # distance = p.findall(disElem.text)
        # print(distance)

    except Exception as e:
        print(e, store)
    #     if e == 'Message: no such element: Unable to locate element: {"method":"css selector","selector":"#panel01 > div > div.sc_box.contact > div.contact_area > div.txt > div > span"}':
    #         distance = None
    #         price = 0
        # if e == 'Message: no such element: Unable to locate element: {"method":"css selector","selector":".count"}':
        #     nreview = 0

    # dic = dict(naver_idx=int(id[j]), r_name=store, r_category='카페', price=price, image_url='https://store.naver.com/restaurants/detail?id='+str(id[j]), distance=0, site_score=0, site_review=nreview, main_menu=menu)
    # info.append(dic)
# for inf in info:    
#     print(inf['naver_idx'],inf['r_name'],inf['r_category'],inf['price'])


# connection = cx_Oracle.connect('scott','tigertiger','orcl.c2yvx9kfplxi.ap-northeast-2.rds.amazonaws.com:1521/orcl')
# # print(connection)
# cur = connection.cursor()
# query = '''
# insert into restaurant(naver_idx, r_name, r_category, price, image_url, distance, site_score, site_review, main_menu)
# values(:naver_idx, :r_name, :r_category, :price, :image_url, :distance, :site_score, :site_review, :main_menu)
# '''

# for inf in info:         
#     cur.execute(query,[int(inf['naver_idx']), inf['r_name'], inf['r_category'],inf['price'], inf['image_url'], int(inf['distance']), int(inf['site_score']), int(inf['site_review']), inf['main_menu']])

# connection.commit()
# connection.close()


# time.sleep(2)