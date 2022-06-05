nome = 'Renato'
idade = 27
altura = 1.81
peso = 89
ano_atual = 2022
nascimento = ano_atual - idade
imc = peso / altura ** 2
print(f'{nome} tem {idade} anos de idade, {altura} de altura,')
print(f'{nome} pesa {peso} kg e seu imc é {imc:.2f}')
print(f'{nome} nasceu em {nascimento}')