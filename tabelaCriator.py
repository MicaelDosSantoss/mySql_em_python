from server import mydb

cursor = mydb.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Carros(id VARCHAR(255) NOT NULL PRIMARY KEY, carro VARCHAR(255) NOT NULL, placa VARCHAR(255) NOT NULL )")
cursor.execute("CREATE TABLE IF NOT EXISTS Users(id VARCHAR(255) NOT NULL PRIMARY KEY, nome VARCHAR(255) NOT NULL, idade VARCHAR(11) NOT NULL, email VARCHAR(255) NOT NULL, sexo ENUM('Masculino','Feminino') NOT NULL )")

# IF NOT EXISTS é comando para ser usando na criação de tabelas, ele funciona da seguinte forma, caso a tabela já tenha sido criada elew n a criara dnv, dessa forma n vai haver erro no codigo
# mycursor.execute para executar os comandos das tabelas

mydb.commit()

mydb.close()