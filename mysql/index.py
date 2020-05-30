import MySQLdb


db = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='wutong',
    charset='utf8'
)
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s " % data)
# SQL 查询语句
sql = "SELECT usr FROM wutong_admin"
try:
    cursor.execute(sql)
    ret = cursor.fetchall()
    print(ret)
except:
    print("Error: unable to fecth data")


db.close()
