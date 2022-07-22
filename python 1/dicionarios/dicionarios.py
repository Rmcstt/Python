d1 = {'chave1': 'valor da chave'}  # cria um dicionário
d1['nova chave'] = 'valor da nova chave'  # adiciona um novo item ao dicionário
d3 = dict(chave3='valor da chave 3', chave4='valor da chave4')  #cria um dicionario com duas chaves
d4 = {'chave1':'valor 1', 'chave1':'valor 2', 'chave1':'valor 3'}  # cria um dicionário com chave repetida
d5 = {1 : 'valor 1', 2 : 'valor 2', 3 : 'valor 3'}  # cria um dicionário com chave numérica
d6 = {1 : 'valor 1', 2 : 'valor 1', 3 : 'valor 1'}
d7 = {'str': 'valor 1',123 : 'valor 2',(1,2,3): 'tupla'}  # cria um dicionário com chave de tipo diferente

print(d1['chave1'])  # valor da chave
print(d1['nova chave'])  # valor da nova chave
print(d3)  # {'chave3': 'valor da chave 3', 'chave4': 'valor da chave4'}
print(d4)   # {'chave1': 'valor 3'}
print(d5)  # {1: 'valor 1', 2: 'valor 2', 3: 'valor 3'}
print(d6)  # {1: 'valor 1', 2: 'valor 1', 3: 'valor 1'} a chave nao pode repetir mas o valor sim!!!
print(d7)  # {'str': 'valor 1', 123: 'valor 2', (1, 2, 3): 'tupla'}
print(d7[(1,2,3)])  #tupla