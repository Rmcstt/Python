nome = input('digite seu nome...: ')

tamanho = len(nome)

if tamanho <=4:
    print('seu nome é curto.')
elif tamanho <=6:
    print('seu nome é normal.')
else:
    print('seu nome é muito grande.')