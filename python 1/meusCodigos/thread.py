import time
import threading
import random

contador = []

def corrida(velocidade, corredores):
  trajeto = 0
  global contador
  while trajeto <= 100 and not contador:
    trajeto += velocidade * random.randint(1,10)
    time.sleep(0.5)
    print(f'corredor: {corredores} km {trajeto}')
    if trajeto >= 100 and contador == []:
      print(f' corredor {corredores} ganhou')
      contador = [corredores]
      break
    else:
      continue

    
def main():
  lista = ['jeff', 'renato']
  for corredores in lista:
    t = threading.Thread(target=corrida, args=(1, corredores))
    t.start()

if __name__ == '__main__':
  main()


  
 

