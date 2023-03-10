import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="testemy"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE carros(id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, carro VARCHAR(255) NOT NULL, placa VARCHAR(255) NOT NULL )")

mycursor.execute("CREATE TABLE users(id INT AUTO_INCREMENT NOT NULL PRIMARY KEY, nome VARCHAR(255) NOT NULL, idade INT NOT NULL, email VARCHAR(255) NOT NULL)")



# mycursor.execute("SELECT * FROM tabela_teste")

# result = mycursor.fetchall()

# for row in result:
#   print(row)
