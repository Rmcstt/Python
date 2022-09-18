from dataclasses import dataclass 

@dataclass(eq=True, order=True, frozen=False, repr=True, init=True)
# itens a serem colocados como parametros do dataclass
#eq=True : compara se os objetos sao iguais
#order=True : compara se um objeto é maior ou renor que o outro
#frozen=true : nao permite que os objetos sejam alterados (__post_init__ , etc)
#repr=True :morstra a representação do objeto
#init=true : inicializa o objeto
#unsafe_hash=True : permite que o objeto seja usado como chave de um dicionario


class Pessoa:
  nome :str = 'renato'
  idade :int = 27
  sobrenome :str = 'mota costa'
  # corDaPele :str = 'branca'
  # profissao :str = 'programador'
  # altura :float = 1.80

  def __post_init__(self):  # metodo especial que roda depois do __init__
    if not isinstance(self.nome, str):
      raise TypeError(f'tipo invalido {type(self.nome).__name__} != str em {self}')

  @property
  def nome_completo(self):
    return f'{self.nome} {self.sobrenome}'

p2 = Pessoa('b', 'renato')
p3 = Pessoa('e', 'renato')
p4 = Pessoa('d', 'renato')
p5 = Pessoa('c', 'renato')
p6 = Pessoa('a', 'renato')


pessoas = [p2, p3, p4, p5, p6]

print(sorted(pessoas))