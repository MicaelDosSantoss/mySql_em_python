import uuid

# uma biblioteca que gera Ids aleatórios 

uid = uuid.uuid4()

sqlCar = "INSERT INTO Carros (id, carro, placa) VALUES (%s, %s, %s)"

c = str('corsa')
p = str.upper('hdaj123')

# Acabei tirando o input do c é o p para não se repetir a mesma pergunta sempre, por enquanto

# c é o são as perguntas para o usuario

# str.upper faz as suas letras ficarem em maisculo

if c and p is not None: insertCar = (str(uid),c ,p)


# Dados users
