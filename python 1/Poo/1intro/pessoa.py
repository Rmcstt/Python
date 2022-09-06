"""
classes sao equivalentes a moldes ou molduras de objetos


padrao de escrita em python
snake case: usado para nomes variaveis e funcoes
pascal case: usado para nomes de classes e metodos
"""
from datetime import datetime


class Pessoa:
  anoAtual = int(datetime.strftime(datetime.now(), '%Y'))


  def __init__(self, nome, idade, comendo= False, falando= False):  # serve para referenciar o objeto que esta sendo chamado
    self.nome = nome
    self.idade = idade
    self.comendo = comendo
    self.falando = falando


  def falar(self, assunto):
    if self.comendo:
      print(f'{self.nome} nao pode falar enquanto esta comendo!!!')
      return
    
    if self.falando:
      print(f'{self.nome} ja disse algo!!!')
      return

    print(f'{self.nome} esta falando... {assunto}...')
    self.falando = True

  def pararFalar(self):
    if not self.falando:
      print(f'{self.nome} nao esta falando nada!!!')
      return

    print(f'{self.nome} parou de falar...')
    self.falando = False



  def comer(self, alimento):
    if self.comendo:
      print(f'callma ai, {self.nome} já esta comendo algo!!!')
      return

    if self.falando:
      print(f'{self.nome} nao pode comer enquanto esta falando!!!')
      return
    print(f'{self.nome} esta comendo um(a) {alimento}...')
    self.comendo = True

    

  def pararComer(self):
    if not self.comendo:
      print(f'{self.nome} já nao esta comendo nada!!!')
      return

    print(f'{self.nome} parou de comer...')
    self.comendo = False


  def getAnoNascimento(self):
      print(self.anoAtual - self.idade)

  
  

  

  

