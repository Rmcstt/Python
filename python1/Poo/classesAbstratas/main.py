"""
classes abstratas = classes que nao podem ser instanciadas, normalmente sao usadas como base para outras classes
para criar basta importar do abc o ABC e o abstractmethod colocar "ABC" como parametro desta classe Ex: class Conta(ABC)
ja o abstractmethod serve para definir um metodo abstrato, ou seja, um um metodo que deve ser implementado nas classes filhas!!!
"""

from classes.poupanca import Poupanca
from classes.corrente import Corrente


cp = Poupanca(123, 1, 1000)
cp.depositar(100)
cp.sacar(500)
cp.sacar(601)
print()
print()

cc = Corrente(123, 2, 2000)
cc.depositar(100)
cc.sacar(2500)
cc.depositar(1500)

