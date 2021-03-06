from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
from pathlib import Path
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


info = []
# 정보 뽑아오기  
for j in range(len(id)):       
    try:
        browser.get(url+id[j])
        time.sleep(1)

        storeElem = browser.find_element_by_css_selector('#content > div:nth-child(1) > div.biz_name_area > strong')
        store = storeElem.text
        # print(store)

        menuElem = browser.find_element_by_css_selector('#content > div:nth-child(2) > div.bizinfo_area > div > div.list_item.list_item_menu > div > ul > li:nth-child(1) > div > div > div > span.name')
        menu = menuElem.text
        # print(menu)
        
        priceElem = browser.find_element_by_css_selector('#content > div:nth-child(2) > div.bizinfo_area > div > div.list_item.list_item_menu > div > ul > li:nth-child(1) > div > em')       
        price = priceElem.text

        nreviewElem = browser.find_element_by_class_name('count')       
        nreview = nreviewElem.text

        # res = requests.get(url+id[j])
        # res.raise_for_status()
        # soup = bs(res.text.'lxml')
        disElem = browser.find_element_by_css_selector('#panel01 > div > div.sc_box.contact > div.contact_area > div > div > ul:nth-child(2)')
        distance = disElem.text[5:10]

        url1 = 'https://store.naver.com/restaurants/detail?entry=pll&id='+str(id[j])
        # container > div.top_photo_area_wrap > div > div > div:nth-child(3) > div > div:nth-child(4) > div > a > img
        # #container > div.top_photo_area_wrap > div > div > div:nth-child(3) > div > div:nth-child(1) > div > a > img
        # print(url1)
        res = requests.get(url1)
        res.raise_for_status()      
        soup = bs(res.text,'lxml')
        # print(soup)
        blog = soup.find("li",attrs={"class":"type_review"})
        if blog:
            blog2 = blog.find("div",attrs={"class":"thumb"})         # <div class='thumb'>를 포함한 모든 내용 가져옴
            img = blog2.find('img')['src']       # <img src= 이하의 값을 가져옴
            print(img)
        else:
            img = "없음"
            print(img)

    except Exception as e:
        if e == 'Message: no such element: Unable to locate element: {"method":"css selector","selector":"#content > div:nth-child(2) > div.bizinfo_area > div > div.list_item.list_item_menu > div > ul > li:nth-child(1) > div > div > div > span.name"}':
            menu = ''
            price = 0
        if e == 'Message: no such element: Unable to locate element: {"method":"css selector","selector":".count"}':
            nreview = 0

    dic = dict(naver_idx=int(id[j]), r_name=store, r_category='카페', price=price, image_url=img, distance=distance, site_score=0, site_review=nreview, main_menu=menu)
    info.append(dic)
# count = 1    
# for inf in info:    
#     print(count, inf)
#     print('------------------------------------')
#     count += 1


connection = cx_Oracle.connect('scott','tigertiger','orcl.czq0cxsnbcns.ap-northeast-2.rds.amazonaws.com:1521/orcl')      # 민수씨 db접속
# connection = cx_Oracle.connect('scott','tigertiger','orcl.c2yvx9kfplxi.ap-northeast-2.rds.amazonaws.com:1521/orcl')      # 내껄로 잠깐 db접속
# print(connection)
cur = connection.cursor()


# 조장님이 짜줌
select_query = '''
select * from restaurant where naver_idx = :naver_idx
'''
#
update_query = '''
UPDATE restaurant SET 
r_name= :r_name, 
r_category= :r_category, 
price= :price, 
image_url= :image_url, 
distance= :distance, 
site_score= :site_score, 
site_review= :site_review, 
main_menu= :main_menu
WHERE naver_idx = :naver_idx
'''
insert_query = '''
INSERT INTO restaurant(naver_idx, r_name, r_category, price, image_url, distance, site_score, site_review, main_menu)
VALUES(:naver_idx, :r_name, :r_category, :price, :image_url, :distance, :site_score, :site_review, :main_menu)
'''


# 조장님이 짜줌
for inf in info:
    cur.execute(select_query, {'naver_idx': inf['naver_idx']})
    res = cur.fetchall()        # 네이버 id가 중복되면 값이 담겨있고 아니면 비어 있음
    if len(res) > 0:
    # update
        cur.execute(update_query, [inf['r_name'], inf['r_category'],inf['price'], inf['image_url'], inf['distance'], int(inf['site_score']), int(inf['site_review']), inf['main_menu'], int(inf['naver_idx'])])
        # where문에 있는 변수도 매개변수 순서에 포함시켜야 함)
    else:
    # insert
        cur.execute(insert_query, [int(inf['naver_idx']), inf['r_name'], inf['r_category'],inf['price'], inf['image_url'], inf['distance'], int(inf['site_score']), int(inf['site_review']), inf['main_menu']])
#
connection.commit()
connection.close()


# time.sleep(2)