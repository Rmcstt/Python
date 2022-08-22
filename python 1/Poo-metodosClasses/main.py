"""
metodo de classes x meetodos de instancia
metodo de classe: metodo relacionado a classe (molde em geral)
metodo de instancia: especifico de cada objeto (mais especifico)
"""

from pessoa import Pessoa

p1 = Pessoa('malaquias', 22)

p2 = Pessoa.por_ano_nascimento('ronaldo', 1950)
print(p2)
print(p2.nome, p2.idade)

p2.get_ano_nascimento()