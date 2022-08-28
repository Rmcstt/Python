
##############  escritor ################

class Escritor:  
  def __init__(self, nome):  # contrutor
    self.__nome = nome  # atributo privado
    self.__ferramenta = None  


  @property  # getter
  def nome(self):
    return self.__nome

  @property  # getter
  def ferramenta(self):
    return self.__ferramenta


  @ferramenta.setter  # setter
  def ferramenta(self, ferramenta):
    self.__ferramenta = ferramenta


##############  caneta  ################

class Caneta:
  def __init__(self, marca):
    self.__marca = marca


  @property  # getter
  def marca(self):
    return self.__marca

  def escrever(self):
    print('caneta esta escrevendo...')


##############  maquina de escrever  ################

class MaquinaDeEscrever:
  def escrever(self):  # funçãp
    print('maquina esta escrevendo...')
    