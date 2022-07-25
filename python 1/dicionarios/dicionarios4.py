import copy

d1 = {1:'a', 2:'b', 3:'c', 4: ['renato','mota']}

v = d1  # v recebe o valor de d1
print(d1)  # {1: 'a', 2: 'b', 3: 'c', 4: ['renato', 'mota']}
print(v)  # {1: 'a', 2: 'b', 3: 'c', 4: ['renato', 'mota']}


v[1] = 'x'  # altera o valor da chave 1

print(d1)  # {1: 'x', 2: 'b', 3: 'c', 4: ['renato', 'mota']}
print(v)  # {1: 'x', 2: 'b', 3: 'c', 4: ['renato', 'mota']}

# o conceito é que ambos os objetos apontam para o mesmo lugar na memoria do sistema, ou seja, se mudar um ira alterar o outro

c = d1.copy()  # c recebe o valor de d1 (copia rasa)
c[1] = 'valor'  # altera o valor da chave 1
c[4][0] = 'joao'  # altera o valor da chave 4 nos dois dicionarios (d1 e c) pello simples fato de (copy()) poder alterare o valor de uma lista e ate mesmo um dicionario que esta dentro de um dicionario, exceto tuplas(são imutaveis).

print(d1)  # {1: 'x', 2: 'b', 3: 'c', 4: ['joao', 'mota']}🟡
print(c)  # {1: 'valor', 2: 'b', 3: 'c', 4: ['joao', 'mota']}🟡

#agora quando usamos deep copy, ele gera realmente um novo objeto, ou seja, se mudar um nao altera o outro, ate mesmo a lista.

d = copy.deepcopy(d1)  # d recebe o valor de d1 (copia profunda)
d[4][0] = 'pedrinho'  # altera  a lista somente no dicionario d


print(d1)  # {1: 'x', 2: 'b', 3: 'c', 4: ['joao', 'mota']}
print(d)  # {1: 'x', 2: 'b', 3: 'c', 4: ['pedrinho', 'mota']}