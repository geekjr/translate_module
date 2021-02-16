import mysql.connector
from easynmt import EasyNMT
import requests
import json


model = EasyNMT('opus-mt')


db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Fadodo24",
        database="chitest",
    )
cursor = db.cursor()
cursor.execute("SHOW COLUMNS FROM chitestnew;")
columns_cursor = cursor.fetchall()
columns = []
for column in columns_cursor:
    columns.append(column[0])
cursor.execute(f"SELECT * FROM chitestnew")
result = cursor.fetchall()
main = []
translated_final = {}
for x in result:
    column_id = 0
    for y in x:
        translated_final.update({columns[column_id]: y})
        column_id += 1
print(translated_final)


url = 'http://52.152.216.112/json'
myobj = json.dumps({"我的爸爸": "我的妈妈"})

x = requests.post(url, data=myobj)

print(x.content)

to_return = "INSERT INTO customers (name, address) VALUES (%s, %s)"