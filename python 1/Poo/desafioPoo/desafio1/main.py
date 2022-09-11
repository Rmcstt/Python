from classes.banco import Banco
from classes.cliente import Cliente
from classes.contas import Conta, Corrente, Poupanca

banco = Banco()

cliente1 = Cliente(input('nome: '), input('idade: '))