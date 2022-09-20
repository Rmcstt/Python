class Minhalista:  # classe que implementa um iterador
  def __init__(self):  # construtor
    self.__items = []
    self.__index = 0

  def add(self, valor):  # metodo para adicionar um item
    self.__items.append(valor)

  def __getitem__(self, index):  # metodo para acessar um item
    return self.__items[index]

  def __setitem__(self, index, valor):  #metodo para alterar um item
    if index >= len(self.__items):
      self.__items.append(valor)
    self.__items[index] = valor

  def __delitem__(self, index):  # metodo para deletar um item
    del self.__items[index]

  def __iter__(self):  # cria um iterador
    return self

  def __next__(self):  # retorna o proximo item
    try:
      item = self.__items[self.__index]
      self.__index += 1
      return item
    except IndexError:
      raise StopIteration


  def __str__(self):  # retorna uma representação de uma string
    return f'{self.__class__.__name__}({self.__items})'

  def __repr__(self):  # retorna uma repressentação para o desenvolvedor
    return self.__str__()


if __name__ == "__main__":  # se o arquivo for executado diretamente...a
  lista = Minhalista()
  lista.add('renato')
  lista.add('maria')

# print(next(lista))
# print(next(lista))

  # for item in lista:
  #   print(item)

  # print(lista)
  # lista[0] = 'joao'
  # lista[2] = 'ciclano'
  # print(lista)

  # del lista[2]

  # lista = list(lista)  # converte o iterador em uma lista

  

  for item in lista:
    print(item)
  for item in lista:
    print(item)
  for item in lista:
    print(item)

  

  