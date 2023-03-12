import uuid

# uma biblioteca que gera Ids aleatórios 

uid = uuid.uuid4()


sqlCar = "INSERT INTO Carros (id, carro, placa) VALUES (%s, %s, %s)"

c = str(input('Qual o seu carro :'))
p = str.upper(input('Qual é a sua placa :'))

# c é o são as perguntas para o usuario

# str.upper faz as suas letras ficarem em maisculo

insertCar = (str(uid),c ,p)

