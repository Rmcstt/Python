from time import sleep
from threading import Thread
import os

def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)

if os.name == 'posix':
    cls = "clear"
else:
    cls = "cls"

t1 = Thread(target=vai_demorar, args=('sucessfull', 10))
t1.start()

while t1.is_alive():
    os.system(cls)
    print('hacking the system')
    sleep(.5)
    os.system(cls)
    print('hacking the system.')
    sleep(.5)
    os.system(cls)
    print('hacking the system..')
    sleep(.5)
    os.system(cls)
    print('hacking the system...')
    sleep(.5)
    os.system(cls)
    print('hacking the system....')
    sleep(.5)