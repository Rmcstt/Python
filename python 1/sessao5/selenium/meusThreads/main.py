from time import sleep
from threading import Thread
import os

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

def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


if os.name == 'posix':
    cls = "clear"
else:
    cls = "cls"

t1 = Thread(target=vai_demorar, args=('concluido', 10))
t1.start()

while t1.is_alive():
    os.system(cls)
    print('processando')
    sleep(.5)
    os.system(cls)
    print('processando.')
    sleep(.5)
    os.system(cls)
    print('processando..')
    sleep(.5)
    os.system(cls)
    print('processando...')
    sleep(.5)
    os.system(cls)
    print('processando....')
    sleep(.5)
    
  
