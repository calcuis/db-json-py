import sqlite3, json

connection = sqlite3.connect("data.db")
cursor = connection.cursor()
cursor.execute("select * from data")
data = cursor.fetchall()
open('data.json', 'w', encoding='utf-8-sig').write(json.dumps(data, indent=4))

connection.close()
