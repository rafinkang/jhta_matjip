# import pyautogui

# print(pyautogui.position())
# from classes/db_conn import *


import sys
sys.path.append('.')
from classes.DbConn import *

db = DbConn()
print(db.execute("SELECT * FROM dept"))