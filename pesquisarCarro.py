from server import mydb
# importando o servidor para esse arquivo

cursor = mydb.cursor()

print('{}'.format("=" * 20))
r = str(input('Qual carro vc deseja: '))

# pegunta, irei mudar futuramente

print('{}'.format("=" * 20))


cursor.execute("SELECT carro,placa FROM `carros` WHERE carro = %s;",(r,) )
# executar o codigo no MySql, para pegar um id

res = cursor.fetchone()


print("Carro disponível : ",res)
# imprimir o resultado

# fetchone() para imprimir uma unica linha do codigo, usado para pegar um unico valor

mydb.commit()
# comitar codigos 

mydb.close()