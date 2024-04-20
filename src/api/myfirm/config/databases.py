import mysql.connector as sql

try:
    s = sql.connect(host = "localhost",user = "root", passwd = "", database = "nucleus_teq")
    cursor = s.cursor()
except Exception as e:
    print(e)
else:
    print("Successfully Connected !!!")
