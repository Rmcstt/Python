from dataclasses import dataclass 

@dataclass()
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
    self.nome_completo = f'{self.nome} {self.sobrenome}'

  # @property
  # def nome_completo(self):
  #   return f'{self.nome} {self.sobrenome}'

p1 = Pessoa()
p2 = Pessoa()

print(p1)
print(p1 == p2)

# print(p1.nome_completo)