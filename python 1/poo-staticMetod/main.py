from pessoa import Pessoa

p1 = Pessoa('malaquias', 22)

p2 = Pessoa.por_ano_nascimento('ronaldo', 1950)  # chamando o metodo de classe
print(p2)
print(p2.nome, p2.idade)

p2.get_ano_nascimento()  # chamando o metodo de instancia

print(Pessoa.gera_id())  # chama o metodo estatico