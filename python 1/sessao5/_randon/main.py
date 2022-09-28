import random
import string
# gera um numero aleatoria entre a e b
#inteiro = random.randint(10,20)

# gera um numero aleatorio usando a funcao range enre a e b com intervalo de c
#inteiro = random.randrange(10,20,2)

# gera um numero de ponto flurtuante enrte a e b
# flutuante = random.uniform(10,20)

# gera um numero de ponto flutuante entre 1 e 0
#flutuante = random.random()



#----------------------------------------------#



# choice  faz um sorteio de uma lista de elementos
# choices faz um sorteio de uma lista de elementos com repeticao
# jokenpo = ['pedra','papel','tesoura']

# jogador1 = random.choice(jokenpo)
# jogador2 = random.choice(jokenpo)

# print(f'jogador 1 {jogador1}')
# print(f'jogador 2 {jogador2}')
# print()
# if jogador1 == jogador2:
#     print('Empate')
# elif jogador1 == 'pedra' and jogador2 == 'tesoura':
#   print('jogador 1 venceu')
# elif jogador1 == 'tesoura' and jogador2 == 'papel':
#   print('jogador 1 venceu')
# elif jogador1 == 'papel' and jogador2 == 'pedra':
#   print('jogador 1 venceu')
# else:
#   print('jogador 2 venceu')


#----------------------------------------------#


# lista = ['joao','maria', 'pedro', 'jose', 'marcos', 'ana', 'carlos', 'julia', 'josefa', 'josefina']

#sorteio = random.choices(lista, k=3)

# ou

##for i in range(1000):
  # sorteio = random.sample(lista, 3)

  # print(sorteio)
# random.shuffle(lista)
# print(lista)

#----------------------------------------------#

# gera senha aleatoria
letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%&*()_+'

todos = letras + digitos + caracteres

tamanho = 20

senha = ''.join(random.sample(todos, k=tamanho))
# choices ou sample

print(senha)