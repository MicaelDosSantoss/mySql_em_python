import mysql.connector
import inserir

# Biblioteca que realiza a conexão do MYsql com o Python, esse biblioteca está no pip uma biblioteca do python


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="testemy"
)

# mysql.connector.connect realiza a conexão com o seu database

mycursor = mydb.cursor()

# mydb.cursor para utilizar o comando das bibliotecas


mycursor.execute("CREATE TABLE IF NOT EXISTS Carros(id VARCHAR(255) NOT NULL PRIMARY KEY, carro VARCHAR(255) NOT NULL, placa VARCHAR(255) NOT NULL )")
mycursor.execute("CREATE  TABLE IF NOT EXISTS Users(id VARCHAR(255) NOT NULL PRIMARY KEY, nome VARCHAR(255) NOT NULL, idade INT NOT NULL, email VARCHAR(255) NOT NULL)")

# IF NOT EXISTS é comando para ser usando na criação de tabelas, ele funciona da seguinte forma, caso a tabela já tenha sido criada elew n a criara dnv, dessa forma n vai haver erro no codigo
# mycursor.execute para executar os comandos das tabelas

mycursor.execute(inserir.sqlCar, inserir.insertCar)
# Esse comando inseri dados no banco de dados, a outra parte está em inserir.py

mydb.commit()
# commit | nele é realizado as alterações de forma automatica

print(mycursor.rowcount, "registro(s) inserido(s)")

mydb.close()
