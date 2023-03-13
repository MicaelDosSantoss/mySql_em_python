import uuid

uid = uuid.uuid4()

sqlUser = "INSERT INTO Users (id, nome, idade, email, sexo) VALUES(%s, %s, %s, %s, %s)"

userName = str("Micael")
userIdade = str("18")
userEmail =str("jwqkf@gmail.com")
userSexo = str('"Masculino"')

inserirUser = (str(uid), userName, userIdade, userEmail, userSexo)

# Esse arquivo faz as inserção de arquivos assim como o primeiro arquivo de inserir