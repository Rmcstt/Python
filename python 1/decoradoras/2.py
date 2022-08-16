from time import time, sleep  # importa a funcao time() e a funcao sleep()

def velocidade(funcao):  # funcao decoradora
  def interna(*args, **kwargs):  # funcao interna
    startTime = time()  # tempo de inicio
    resultado = funcao(*args, **kwargs)  # executa a funcao
    endTime = time()  # tempo de fim
    tempo = (endTime - startTime) * 1000  # calcula o tempo gasto
    print(f'\na funcao {funcao.__name__}'  # mostra o nome da funcao
    f' levou {tempo:.4f} ms para executar')  # mostra o tempo gasto
    return resultado  # retorna o resultado
  return interna  # retorna a funcao interna

 
@velocidade  # chama a funcao decoradora
def demora():  # funcao que sera decorada
  for i in range(10):  # loop que faz o calculo
    print(i, end='')  # mostra o valor do loop
    


demora()
