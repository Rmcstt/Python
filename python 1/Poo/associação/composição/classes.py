class Cliente:
  def __init__(self, nome, idade):
    self._nome = nome
    self._idade = idade
    self._enderecos = []

  @property  # getter para pegar o "nome" que esta privado
  def nome(self):
    return self._nome

  def inserir_endereco(self, cidade, estado):
    self._enderecos.append(Endereco(cidade, estado))

  def lista_enderecos(self):
    for endereco in self._enderecos:
      print(endereco._cidade, endereco._estado)

  def __del__(self):
    print(f'{self._nome} foi apagado')



class Endereco:
  def __init__(self, cidade, estado):
    self._cidade = cidade
    self._estado = estado

  @property
  def cidade(self):
    return self._cidade

  @property
  def estado(self):
    return self._estado

  def __del__(self):
    print(f'{self.cidade}/{self.estado} foi apagado')

