import mysql.connector as sql_connector

try:
    sql = sql_connector.connect(host = "localhost",user = "root", passwd = "", database = "nucleus_teq")
    cursor = sql.cursor()
except Exception as e:
    print(e)
else:
    print("Successfully Connected !!!")
