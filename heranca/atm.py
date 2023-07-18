import conta


usuario = conta.Conta(123, "Nico", 55.5, 1000.0)
usuario2 = conta.Conta(231, "Ze", 40, 1000.0)

print(usuario)

print("imprimindo atributo titular {}".format(usuario.titular))

#Chamando o setter
usuario.saldo = 100

usuario.extrato()
usuario2.extrato()

usuario.transferir(usuario2,10)

usuario.extrato()
usuario2.extrato()
