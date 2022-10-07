from time import sleep
from threading import Thread
from threading import Lock
import os
import random 

# print('ola')

# for i in range(10):
#   print(i)
#   sleep(.25)

# print('mundo')

#----------------------------------------------#

# class MeuThread(Thread):
#   def __init__(self, texto, tempo):
#     self.texto = texto
#     self.tempo = tempo

#     super().__init__()

#   def run(self):
#     sleep(self.tempo)
#     print(self.texto)


# t1 = MeuThread('Thread 1', 2)
# t1.start()
# t2 = MeuThread('Thread 2', 5)
# t2.start()
# t3 = MeuThread('Thread 3', 7)
# t3.start()

# for i in range(20):
#   print(i)
#   sleep(1)

#----------------------------------------------#


# def vai_demorar(texto, tempo):
#   sleep(tempo)
#   print(texto)

# t1 = Thread(target=vai_demorar, args=('oi', 4))
# t1.start()

# t2 = Thread(target=vai_demorar, args=('tudo bem?', 5))
# t2.start()

# t3 = Thread(target=vai_demorar, args=('tchau', 8))
# t3.start()

# for i in range(1,20):
#   print(i)
#   sleep(.5)


#----------------------------------------------#

class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print('Nao temos ingressos suficientes')
            self.lock.release()
            return

        
        sleep(1)


        self.estoque -= quantidade
        print(f'voce comprou {quantidade} ingressos, ainda temos: {self.estoque} ingressso(s)')

        self.lock.release()
  
if __name__=='__main__':
    ingressos = Ingressos(10)
    lista_threads = []


    for i in range(10):
        sorte = random.randint(1, 3)
        t = Thread(target=ingressos.comprar, args=(sorte,))
        lista_threads.append(t)

    for t in lista_threads:
        t.start()
    for thread in lista_threads:
        thread.join()


    executando = True
    while executando:
        executando = False
        if t in lista_threads:
            executando = True
            break

    print(f'ainda temos {ingressos.estoque} ingressos')
