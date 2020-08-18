import cx_Oracle
""" 
민수 DB
orcl.czq0cxsnbcns.ap-northeast-2.rds.amazonaws.com, orcl, scott, tigertiger, 1521
""" 

class DbConn:
    def __init__(
        self, 
        host = "orcl.czq0cxsnbcns.ap-northeast-2.rds.amazonaws.com", 
        dbname = "orcl", 
        user = "scott", 
        password = "tigertiger", 
        port = "1521"
        ):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.port = port
        self.connection = cx_Oracle.connect(self.user, self.password, self.host+":"+self.port+"/"+self.dbname)

    def execute(self, sql):
        self.sql = sql
        cur = self.connection.cursor()
        cur.execute(sql)
        resultList = cur.fetchall()
        self.connection.close()
        return resultList

# db = DbConn()
# print(db.execute("SELECT * FROM dept"))
