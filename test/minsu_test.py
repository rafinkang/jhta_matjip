import requests
import time
import pyautogui
import pyperclip
from bs4 import BeautifulSoup as bs
from pprint import pprint
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# NAVER_IDX = []
# R_NAME = []
# R_CATEGORY = []
# PRICE = []
# IMAGE_URL = []
# DISTANCE = []
# SCORE = []
# SITE_SCORE = []
# REVIEW = []
# SITE_REVIEW = []
# MAIN_MENU = []
dict_list = []

url_place = "https://store.naver.com/restaurants/detail?entry=pll&id="

url = "https://store.naver.com/restaurants/list?entry=pll&filterId=r09110133&query=%EC%9D%B5%EC%84%A0%EB%8F%99%20%EB%A7%9B%EC%A7%91&sessionid=%2FQDp24r%2FMXU9PW%2Fnrrt2fZQk"
browser = webdriver.Chrome("E:\dev\python_workspace\chromedriver.exe")
browser.get(url)

# 화면 최대화
browser.maximize_window()
time.sleep(1)

elem = browser.find_element_by_css_selector("#container > div.placemap_area > div.list_wrapper > div > div.list_area > ul")
# print(elem.text)
li_list = elem.find_elements_by_css_selector('li')

cnt = 0
for store in li_list:
    cnt += 1
    print(cnt,"번째 for문 실행중")

    url_id = store.find_element_by_css_selector('a').get_attribute('href')
    query_pos = url_id.find("query")
    id_pos = url_id.find("id")
    NAVER_IDX = url_id[id_pos+3:query_pos-1]
    # print(bussiness_id)
    # 리스트에 각 식당의 네이버 id 입력
    
    

    IMAGE_URL = url_place + NAVER_IDX
    res = requests.get(IMAGE_URL) # 나중에 여기는 i로 바꿔줘야함
    res.raise_for_status()
    # pprint(res.text)
    # /t 이런것들 나오는 썡 코드

    soup = bs(res.text,'lxml')
    # pprint(soup)
    # /t 이런거 없애준 예쁜 코드

    R_NAME = soup.find("strong",attrs={"class","name"}).text
    # pprint(name)
    

    R_CATEGORY = soup.find("span",attrs={"class","category"}).text
    # pprint(cate)
    

    price = soup.find("em",attrs={"class","price"}).text
    price_num = price.find(",")
    PRICE = int(price[:price_num]+"000")
    # pprint(price)
    

    dis = soup.find("div",attrs={"class","contact_area"}).text
    print(dis)
    dis_dobo = dis.find("도보")
    dis_bun  = dis.find("분")
    DISTANCE = dis[dis_dobo+3:dis_bun+1]
    # print(DISTANCE)
    
    
    raing_area = soup.find("div",attrs={"class","raing_area"})
    if raing_area:
        score = raing_area.find("span",attrs={"class","score"})
        # print(score)
        SITE_SCORE = score.find("em",).text
    else:
        SITE_SCORE = 0
    # print(score2)
    

    reviews = soup.find("div",attrs={"class","info_inner"})
    reviews2 = reviews.find_all("a",attrs={"class","link"})
    SITE_REVIEW = 0
    for rev in reviews2:
        SITE_REVIEW += int(rev.text[7:])
    # print(cnt)    
    

    menu = soup.find("div",attrs={"class","menu_area"})
    MAIN_MENU = menu.find("span",attrs={"class","name"}).text
    # print(menu2)
    
    dict_list.append({
        'NAVER_IDX' : NAVER_IDX,
        'R_NAME' : R_NAME,
        'R_CATEGORY' : R_CATEGORY,
        'PRICE' : PRICE,
        'IMAGE_URL' : IMAGE_URL,
        'DISTANCE' : DISTANCE,
        'SITE_SCORE' : SITE_SCORE,
        'SITE_REVIEW' : SITE_REVIEW, 
        'MAIN_MENU' : MAIN_MENU
    })

print(dict_list)