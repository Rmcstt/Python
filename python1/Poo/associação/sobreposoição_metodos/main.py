from classes import Cliente, Aluno, ClienteVip

c1 = Cliente('joana', 22)
a1 = Aluno('joao', 21)
cv1 = ClienteVip('renato', 'mota', 27)




print(c1.nome, c1.idade)
c1.falar()
c1.acao()
print()
print(a1.nome, a1.idade)
a1.falar()
a1.acao()
print()
print(cv1.nome, cv1.sobrenome, cv1.idade)
cv1.falar()
cv1.acao()