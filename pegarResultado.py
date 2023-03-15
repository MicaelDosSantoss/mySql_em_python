from server import mydb

# from é o arquivo que eu vou pegar, como o import eu posso importar um modulo que eu desejo

cursor = mydb.cursor()

# mydb.cursor() server para usar comandos da blibioteca mysql.connector

cursor.execute('SELECT * FROM Carros')

# .execute() para executar as ações

resultado = cursor.fetchall()

for x in resultado:
  print(x)

# esse loop manda os valores para mim, um por um

mydb.commit()

# .commit() para executar a ação no server

mydb.close()