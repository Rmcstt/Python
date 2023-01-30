"""
operador ternario

jeito convencional
"""

logged_user = True

if logged_user:
    msg = 'usuario logado'
else:
    msg = 'o usuario nao esta logado'
print(msg)


"""
jeito pratico
"""

logged_user2 = True

# um pouco compxexo ainda para mim porem muito mais pratico
msg2 = 'user logado' if logged_user2 else 'user nao esta logado'

print(msg2)

"""
sistema de maioridade
"""

idade = input('qual sua idade: ')

if not idade.isnumeric():
    print('voce precisa digitar um numero')
else:
    idade = int(idade)
    print('maior de idade') if idade >= 18 else print('nao é maior de idade')
