
from classes.banco import Banco
from classes.cliente import Cliente
from classes.contas import Conta, Corrente, Poupanca
import os

if os.name == 'posix':
    cls = "clear"
else:
    cls = "cls"


banco = Banco()

os.system(cls)

nome = input('Digite seu nome: ')
nome = nome.capitalize()

os.system(cls)
idade = int(input(f'{nome} digite sua idade: '))


cliente = Cliente(nome, idade)

os.system(cls)

escolhaConta = int(input('Digite 1 para conta corrente ou 2 para conta poupança: '))

os.system(cls)

if escolhaConta == 1:
  conta = Corrente(1111, 1, 0)
elif escolhaConta == 2:
  conta = Poupanca(1111, 1, 0)
else:
  print('Opção inválida')
  exit()

cliente.inserir_conta(conta)
banco.inserir_clientes(cliente)
banco.inserir_contas(conta)


if banco.autenticar(cliente):
  print('Cliente autenticado')
else:
  print('Cliente não autenticado')
  exit()



while True:
  print()
  print('1 - Depositar')
  print('2 - Sacar')
  print('3 - Sair')
  print()
  opcao = int(input(f'{nome} digite a opção desejada: '))
  os.system(cls)
  if opcao == 1:
    valor = float(input('Digite o valor a ser depositado: '))
    cliente.conta.depositar(valor)
  elif opcao == 2:
    valor = float(input('Digite o valor a ser sacado: '))
    cliente.conta.sacar(valor)
  elif opcao == 3:
    print('Obrigado por utilizar nossos serviços')
    exit()
  else:
    print('Opção inválida')





