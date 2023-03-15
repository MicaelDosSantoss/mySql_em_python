from server import mydb
import uuid

cursor = mydb.cursor()

# uma biblioteca que gera Ids aleatórios 

uid = uuid.uuid4()

sqlCar = "INSERT INTO Carros (id, carro, placa) VALUES (%s, %s, %s)"

print('{}'.format("=" * 20))

c = str(input('Qual o seu carro: '))
p = str.upper(input('Número da placa: '))

# Acabei tirando o input do c é o p para não se repetir a mesma pergunta sempre, por enquanto

# c é o são as perguntas para o usuario

# str.upper faz as suas letras ficarem em maisculo

insertCar = (str(uid),c ,p)

cursor.execute(sqlCar,insertCar)

# Dados users

mydb.commit()

mydb.close()