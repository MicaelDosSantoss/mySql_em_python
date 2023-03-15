import mysql.connector

# Biblioteca que realiza a conexão do MYsql com o Python, esse biblioteca está no pip uma biblioteca do python

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="testemy"
)

# mysql.connector.connect realiza a conexão com o seu database


# mydb.cursor para utilizar o comando das bibliotecas


# IF NOT EXISTS é comando para ser usando na criação de tabelas, ele funciona da seguinte forma, caso a tabela já tenha sido criada elew n a criara dnv, dessa forma n vai haver erro no codigo
# mycursor.execute para executar os comandos das tabelas


# Esse comando inseri dados no banco de dados, a outra parte está em inserir.py

# commit | nele é realizado as alterações de forma automatica

# print(mycursor.rowcount, "registro(s) inserido(s)")


