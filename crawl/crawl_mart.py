from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
import sys
import cx_Oracle

# one plus one

url = "https://emart24.co.kr/product/eventProduct.asp"

browser = webdriver.Chrome("e:/dev/python_workspace/chromedriver.exe")

browser.get(url)

browser.maximize_window()

time.sleep(0.5)

pyautogui.click(785,429)

emart24_list = []
emart24_price_list = []
emart24_total = []
emart24_image_list = []

for i in range(19):
    time.sleep(0.1)
    lists = browser.find_elements_by_css_selector("#regForm > div.section > div.eventProduct > div.tabContArea > ul > li")

    for store in lists:
        emart24_list.append(store.find_element_by_css_selector("p.productDiv").text)
        emart24_price_list.append(store.find_element_by_css_selector("p.price").text)
        emart24_image_list.append(store.find_element_by_css_selector("p.productImg > Img").get_attribute('src'))
        price = store.find_element_by_css_selector("p.price").text
        image = store.find_element_by_css_selector("p.productImg > Img").get_attribute('src')
        emart24_total.append({
            'menu' : store.find_element_by_css_selector("p.productDiv").text,
            'price' : price,
            'discount' : price,
            'menu_option' : '1+1',
            'image_url' : image
        })

    pyautogui.scroll(-1200)
    pyautogui.click(1197,727)
    
print(emart24_total)


# two plus one

pyautogui.scroll(1200)

pyautogui.click(889,429)

for i in range(10):
    time.sleep(0.1)
    lists = browser.find_elements_by_css_selector("#regForm > div.section > div.eventProduct > div.tabContArea > ul > li")

    for store in lists:
        emart24_list.append(store.find_element_by_css_selector("p.productDiv").text)
        emart24_price_list.append(store.find_element_by_css_selector("p.price").text)
        emart24_image_list.append(store.find_element_by_css_selector("p.productImg > Img").get_attribute('src'))
        price = store.find_element_by_css_selector("p.price").text
        image = store.find_element_by_css_selector("p.productImg > Img").get_attribute('src')
        emart24_total.append({
            'menu' : store.find_element_by_css_selector("p.productDiv").text,
            'price' : price,
            'discount' : price,
            'menu_option' : '2+1',
            'image_url' : image
        })

    pyautogui.scroll(-1200)
    pyautogui.click(1197,727)

for i in range(30):
    time.sleep(0.1)
    lists = browser.find_elements_by_css_selector("#regForm > div.section > div.eventProduct > div.tabContArea > ul > li")

    for store in lists:
        emart24_list.append(store.find_element_by_css_selector("p.productDiv").text)
        emart24_price_list.append(store.find_element_by_css_selector("p.price").text)
        emart24_image_list.append(store.find_element_by_css_selector("p.productImg > Img").get_attribute('src'))
        price = store.find_element_by_css_selector("p.price").text
        image = store.find_element_by_css_selector("p.productImg > Img").get_attribute('src')
        emart24_total.append({
            'menu' : store.find_element_by_css_selector("p.productDiv").text,
            'price' : price,
            'discount' : price,
            'menu_option' : '2+1',
            'image_url' : image
        })
    pyautogui.scroll(-1200)
    pyautogui.click(1223,727)

for i in range(5):
    time.sleep(0.1)
    lists = browser.find_elements_by_css_selector("#regForm > div.section > div.eventProduct > div.tabContArea > ul > li")

    for store in lists:
        emart24_list.append(store.find_element_by_css_selector("p.productDiv").text)
        emart24_price_list.append(store.find_element_by_css_selector("p.price").text)
        emart24_image_list.append(store.find_element_by_css_selector("p.productImg > Img").get_attribute('src'))
        price = store.find_element_by_css_selector("p.price").text
        image = store.find_element_by_css_selector("p.productImg > Img").get_attribute('src')
        emart24_total.append({
            'menu' : store.find_element_by_css_selector("p.productDiv").text,
            'price' : price,
            'discount' : price,
            'menu_option' : '2+1',
            'image_url' : image
        })
    pyautogui.scroll(-1200)
    pyautogui.click(1143,726)   
    

# sale

pyautogui.scroll(1200)

pyautogui.click(1092,429)

for i in range(7):
    time.sleep(0.1)
    lists = browser.find_elements_by_css_selector("#regForm > div.section > div.eventProduct > div.tabContArea > ul > li")

    for store in lists:
        emart24_list.append(store.find_element_by_css_selector("p.productDiv").text)
        emart24_price_list.append(store.find_element_by_css_selector("p.price").text)
        emart24_image_list.append(store.find_element_by_css_selector("p.productImg > Img").get_attribute('src'))
        total = store.find_element_by_css_selector("p.price").text
        price, discount = total.split("→")
        image = store.find_element_by_css_selector("p.productImg > Img").get_attribute('src')
        emart24_total.append({
            'menu' : store.find_element_by_css_selector("p.productDiv").text,
            'price' : price,          
            'discount' : discount,
            'menu_option' : 'sale',
            'image_url' : image
        })
    
    pyautogui.scroll(-1200)
    pyautogui.click(1155,727)

connection = cx_Oracle.connect("scott","tigertiger","orcl.czq0cxsnbcns.ap-northeast-2.rds.amazonaws.com:1521/orcl")
cur = connection.cursor()

for t in emart24_total:
    print(t['menu'],t['price'],t['discount'],t['menu_option'],t['image_url'])

    sql_select = """
    SELECT menu
    FROM restaurant_menu
    WHERE menu = :menu
    """
    
    cur.execute(sql_select, menu = t['menu'])
    db_result = cur.fetchall()
    db_exist = len(db_result)


    sql_update = """
    UPDATE restaurant_menu SET
        menu = :menu,
        price = :price,
        discount = :discount,
        menu_option = :menu_option,
        image_url = :image_url
    WHERE menu = :menu2
    """
    sql_insert = """
    INSERT INTO restaurant_menu(
        r_idx,
        menu,
        price,
        discount,
        menu_option,
        image_url
    ) VALUES (
        1,
        :menu,
        :price,
        :discount,
        :menu_option,
        :image_url
    )
    """
    
    if db_exist:
        cur.execute(sql_update,
        menu = t['menu'],
        price = t['price'],
        discount = t['discount'],
        menu_option = t['menu_option'],
        image_url = t['image_url'],
        menu2 = t['menu']
        )
    
    else:
        cur.execute(sql_insert,
        menu = t['menu'],
        price = t['price'],
        discount = t['discount'],
        menu_option = t['menu_option'],
        image_url = t['image_url']
        )

connection.commit()
connection.close()






