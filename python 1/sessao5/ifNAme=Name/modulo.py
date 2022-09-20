def soma(x: float, y:float) -> float:
  return x + y

if __name__ == '__main__':  # isso permite que essa função nao seja executada quano o modulo for importado, pois o __name__ aqui sse chama __main__, e quando ele é importado ele passa a ser chamado pelo nome do arquivo!!!
  print(__name__)
  print(soma(3,7))
  print(soma(30,50))

  # da tambem para fazer uma função:
  # def main():
  #  print(__name__)
  #  print(soma(3,7))
  #  print(soma(30,50))

  # if __name__ == '__main__':
  #  main() 


