import requests
import time
import pyautogui
import pyperclip
from bs4 import BeautifulSoup as bs
from pprint import pprint
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


url = "https://map.naver.com/v5/search/%EC%A2%85%EB%A1%9C3%EA%B0%80%2B%EB%A7%9B%EC%A7%91?c=14136582.4684663,4518899.7206992,17,0,0,0,dh"
browser = webdriver.Chrome("E:\dev\python_workspace\chromedriver.exe")
browser.get(url)

# 화면 최대화
browser.maximize_window()
time.sleep(1)

# A 찾아서 누르기
i = pyautogui.locateOnScreen("e:/dev/python_workspace/img/A.png")
pos = pyautogui.center(i) # 그림의 정중앙 좌표
pyautogui.click(pos)

rest_name = browser.find_element_by_xpath('//*[@id="container"]/div[1]/shrinkable-layout/search-layout/search-entry/entry-layout/entry-place/div/div[2]/div/div[1]/div[2]/div[1]/strong/text()')
# print(rest_name)


# matjipList=[]

# for i in range(100): #블로그 70000개 있음, 7000 검색해야함
#     print(i,"번째 시행중")
#     # 종로3가 맛집 검색시 url
#     url ="https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query=%EC%A2%85%EB%A1%9C3%EA%B0%80%20%EB%A7%9B%EC%A7%91&sm=tab_pge&srchby=all&st=sim&where=post&start={}".format(i*10+1)
#     # 주소 뒤에 숫자 1, 11, 21,... 10씩 늘어나야함
#     # url = "https://blog.naver.com/missgyul/222032066556"
#     res = requests.get(url)
#     res.raise_for_status()
#     # pprint(res.text)
#     # # # /t 이런것들 나오는 썡 코드

#     soup = bs(res.text,'lxml')
#     # pprint(soup)
#     # # # /t 이런거 없애준 예쁜 코드

#     r_contents = soup.find_all("dd",attrs={"class","sh_blog_passage"})
#     # pprint(product_names)
#     for r_content in r_contents:
#         r2 = r_content.get_text().split()
#         for r3 in r2:
#             if r3[0] == "#":
#                 if r3 in matjipList:
#                     continue
#                 else:
#                     matjipList.append(r3)
                
