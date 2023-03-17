from server import mydb

cursor = mydb.cursor()

r = str(input('Qual User você deseja, inserir ID: '))

print('{}'.format("=" * 20))
cursor.execute('SELECT * FROM users WHERE id=%s',(r,))

res = cursor.fetchone()

print('Resultado : ',res)



mydb.commit()

mydb.close()