variavel = ['renato mota', 'Joao', 'maria']

comeca_com_j = False
for valor in variavel:
    if valor.lower().startswith('j'):
        comeca_com_j = True

if comeca_com_j:
    print('existe uma palavra que começa com "j"')
else:
    print(' nao começa com j')