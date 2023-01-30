"""
o que sao dataaclasses? o modulo dataclasses fornece um decorador e funcoes para criar automaticamente metodos como:__init__, __repr__, __eq__, __lt__ e outros, em classes definidas pelo usuario.
basicamente, dataclasses sao syntax sugar para criar classes normais.
foi originalmente descrito na PEP 557.
adiciionado na versao 3.7 do Python
leia a documentacao em: https://docs.python.org/3/library/dataclasses.html
"""

from dataclasses import dataclass 

@dataclass
class Pessoa:
  nome :str = 'renato'
  idade :int = 27
  sobrenome :str = 'mota costa'
  corDaPele :str = 'branca'
  profissao :str = 'programador'
  altura :float = 1.80

  @property
  def nome_completo(self):
    return f'{self.nome} {self.sobrenome}'

p1 = Pessoa()

print(p1)
print(p1.nome_completo)