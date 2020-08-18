from classes.DbConn import *

db = DbConn()
print(db.execute("SELECT * FROM dept"))