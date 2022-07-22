d1 = {'str': 'valor 1', 123: 'valor 2', (1, 2, 3): 'tupla'}


d1['naoexiste'] = 'agora existe'  # adiciona um novo item ao dicionário

if 'naoexiste' in d1:  # verifica se a chave existe
    print(d1['naoexiste'])  # agora existe

print(d1.get('outroQNaoexiste'))  # None
