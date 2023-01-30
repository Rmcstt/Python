from classes.banco import Banco
from classes.cliente import Cliente
from classes.contas import Conta, Corrente, Poupanca


banco = Banco()





cliente1 = Cliente('João', 25)
cliente2 = Cliente('Maria', 19)
cliente3 = Cliente('José', 32)
cliente4 = Cliente('Ana', 21)

conta1 = Corrente(1111, 1, 500)
conta2 = Poupanca(2222, 2, 1000)
conta3 = Corrente(3333, 3, 500)
conta4 = Poupanca(1111, 4, 1000)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)
cliente4.inserir_conta(conta4)

banco.inserir_clientes(cliente1)
banco.inserir_clientes(cliente2)
banco.inserir_clientes(cliente3)
banco.inserir_clientes(cliente4)

banco.inserir_contas(conta1)
banco.inserir_contas(conta2)
banco.inserir_contas(conta3)
banco.inserir_contas(conta4)

if banco.autenticar(cliente1):
  cliente1.conta.depositar(100)
  cliente1.conta.sacar(500)
else:
  print('cliente nao autenticado')

if banco.autenticar(cliente2):
  cliente2.conta.depositar(100)
  cliente2.conta.sacar(500)
else:
  print('cliente nao autenticado')

if banco.autenticar(cliente3):
  cliente3.conta.depositar(100)
  cliente3.conta.sacar(500)
else:
  print('cliente nao autenticado')

if banco.autenticar(cliente4):
  cliente4.conta.depositar(100)
  cliente4.conta.sacar(500)
else:
  print('cliente nao autenticado')