import mysql.connector as mc

if __name__ == "__main__":
    sql =  mc.connect(host = "localhost" , user = "root" , passwd= "") 
    mycursor = sql.cursor()

    # Alredy created database nucleus_teq
    # -> mycursor.execute("create database nucleus_teq")
    mycursor.execute("USE nucleus_teq;")
    mycursor.execute("SHOW TABLES;")
    result = mycursor.fetchall()
    print(result)

    # mycursor.execute("""CREATE TABLE demo(
    #                  name varchar(30), 
    #                  id int);""")
    # mycursor.execute("""INSERT INTO demo VALUES
    #                  ('KOMAL',12),
    #                  ('nitin',23);""")
    # sql.commit()
    mycursor.execute("""SELECT * FROM demo;""")
    
    # print(mycursor.fetchone())
    # print(mycursor.fetchone())
    # print(mycursor.fetchone())

    # print(mycursor.fetchall())
    # print(mycursor.fetchall())

    print(mycursor.fetchmany(size = 4))



