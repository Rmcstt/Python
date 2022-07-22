d1 = {'str': 'valor 1', 123: 'valor 2', (1, 2, 3): 'tupla'}  # dicionario


d1['naoexiste'] = 'agora existe'  # adiciona um novo item ao dicionário

if 'naoexiste' in d1:  # verifica se a chave existe
    print(d1['naoexiste'])  # agora existe

print(d1.get('outraChave'))  # None

d1.update({'outraChave': 'valor 3'})  # adiciona um novo item ao dicionario!!!

if d1.get('outraChave') is not None:  # verifica se a chave existe
    print(d1.get('outraChave'))  # valor 3

for k in d1:  # percorre as keys do dicionario
    print(k)  # imprime as chaves 'str', '123', '(1, 2, 3)'

for v in d1:  # percorre os valores do dicionario
    print(v)  # imprime os valores 'valor 1', 'valor 2', 'valor 3'

for x in d1.items():  # percorre os pares chave/valor do dicionario
    print(x[0], x[1])  #chave/valor 

print(d1)  # {'str': 'valor 1', 123: 'valor 2', (1, 2, 3): 'tupla', 'naoexiste': 'agora existe', 'outraChave': 'valor 3'}

del d1['str'] # deleta a chave 'str'

print(len(d1))  # 4   =>   função len() me retorna quantos pares (chave:valor) existem nesse dicionario


print('str' in d1)  # False
print('str' in d1.keys())  #False
print('valor 1' in d1.values()) # False


