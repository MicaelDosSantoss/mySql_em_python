from server import mydb

cursor = mydb.cursor()

cursor.execute('SELECT * FROM users')

Resultado = cursor.fetchall()

for x in Resultado:
    print(x)

mydb.commit()

mydb.close()