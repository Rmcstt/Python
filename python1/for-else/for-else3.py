variavel = ['renato mota', 'Joao', 'maria']

for valor in variavel:
    if valor.lower().startswith('j'):
        continue
    print(valor)
else:
    print('nao existe uma pa;avra que comece com a letra "j" ')

    # renato mota
    # maria
    # nao existe um nome com que comece com a letra "j"