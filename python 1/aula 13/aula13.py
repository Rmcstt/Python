usuario = input('digite seu nome: ')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('voce precisa digitar pelo menos 6 caracteres')
else:
    print('voce foi cadastrado com sucesso')