nome = 'Renato'
idade = 27
altura = 1.81
peso = 89
ano_atual = 2022
nascimento = ano_atual - idade
imc = peso / altura ** 2
print(f'{nome} tem {idade} anos de idade, {altura} de altura,')  # renato tem 27 anos de idade, 1.81 de altura
print(f'{nome} pesa {peso} kg e seu imc é {imc:.2f}')  # renato pesa 89 kg e seu imc é 23.16
print(f'{nome} nasceu em {nascimento}')  # renato nasceu em 1995