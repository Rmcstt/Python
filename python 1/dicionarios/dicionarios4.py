d1 = {1:'a', 2:'b', 3:'c'}

v = d1  # v recebe o valor de d1
print(d1)  # {1: 'a', 2: 'b', 3: 'c'}
print(v)  # {1: 'a', 2: 'b', 3: 'c'}


v[1] = 'x'  # altera o valor da chave 1

print(d1)  # {1: 'x', 2: 'b', 3: 'c'}
print(v)  # {1: 'x', 2: 'b', 3: 'c'}

# o conceito é que ambos os objetos apontam para o mesmo lugar na memoria do sistema, ou seja, se mudar um ira alterar o outro

c = d1.copy()  # c recebe o valor de d1 (copia rasa)
c[1] = 'valor'  # altera o valor da chave 1

print(d1)  # {1: 'x', 2: 'b', 3: 'c'}
print(c)  # {1: 'valor', 2: 'b', 3: 'c'}

#agora quando usamos
