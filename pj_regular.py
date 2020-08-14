from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests
from pathlib import Path
from selenium import webdriver
import re

# brower = webdriver.Chrome()
# brower.get('https://naver.com')
# element = brower.find_element_by_id('query')
# element.click()     # 창을 띄운 후 검색창에 클릭이 됨
# element.send_keys('익선동 카페')       # 검색창에 해당 검색어가 보내짐
# button = brower.find_element_by_id('search_btn')        # 
# button.click()

# brower.close()

url = 'https://store.naver.com/restaurants/list?entry=pll&filterId=r09110133&menu=1&query=%EC%9D%B5%EC%84%A0%EB%8F%99%20%EB%A7%9B%EC%A7%91&sessionid=Eeey0F5Hi%2BYgEoH4EsMEpstB'


res = requests.get(url)
# print(res.text, len(res.text))

res.raise_for_status()      # 만약 에러가 있으면 에러 메세지 출력 후 끝내고 아니면 하위에 코드를 실행

soup = bs(res.text,'lxml')
pprint(soup)

p = re.compile('"id":"[0-9]+","name":"[가-힣]+"')
# print(p,type(p))
store = p.findall(str(soup))
print(store)
# pprint(atags)
# for a in atags:
#     span = a.find('span')
#     print(span.get_text())
