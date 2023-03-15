from server import mydb
import uuid

cursor = mydb.cursor()

uid = uuid.uuid4()

sqlUser = "INSERT INTO Users (id, nome, idade, email, sexo) VALUES(%s, %s, %s, %s, %s)"

userName = str(input('Qual o seu nome: '))
userIdade = str(input('Qual a sua idade: '))
userEmail =str(input('Qual é o seu E-mail:'))
userSexo = str(input('Feminino ou Masculino: '))

inserirUser = (str(uid), userName, userIdade, userEmail, userSexo)

cursor.execute(sqlUser,inserirUser)

mydb.commit()
mydb.close()


# Esse arquivo faz as inserção de arquivos assim como o primeiro arquivo de inserir