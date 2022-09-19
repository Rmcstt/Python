class Minhalista:
  def __init__(self):
    self.__items = []

  def add(self, valor):
    self.__items.append(valor)

  def __iter__(self):
    return iter(self)

  def __next__(self):
    item = self.__items[self.__index]
    self.__index += 1
    return item

  def __str__(self):
    return f'{self.__class__.__name__}({self.__items})'


if __name__ == "__main__":
  lista = Minhalista()
  lista.add('renato')
  lista.add('maria')

  print(lista)

  