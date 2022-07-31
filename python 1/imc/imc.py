from datetime import date  # Importa a biblioteca date
data_atual = date.today()  # Cria uma variável com a data atual


nome = "renato mota"
idade = 26
altura = 1.80
E_maior = idade > 18
ano_nascimento = 1995

peso = 88
imc = (peso / altura ** 2)  # operador de potencia tem peso maior que a propria divisao!!!
print(data_atual.year)  # 2022

print(nome, "tem", idade, "anos de idade, e seu imc é de ", imc)  # renato tem 26 anos de idade, e seu imc é de 23.160493827160494
print(f'{nome} tem {idade} anos de idade, e seu imc é de  {imc:.2f}')  # renato tem 26 anos de idade, e seu imc é de  23.16
# com Fstrings
# ":.2f" = duas casas decimais depois do ponto flutuante(float)
print('{} tem {} anos de idade, e seu imc é de  {:.2f}'.format(nome, idade, imc))  # renato tem 26 anos de idade, e seu imc é de  23.16
# mesmo depois deste ultimo exemplo ainda prefiro o "Fstrings

"""
renato mota tem 26 anos de idade, e seu imc é de  27.160493827160494
renato mota tem 26 anos de idade, e seu imc é de  27.16
renato mota tem 26 anos de idade, e seu imc é de  27.16
"""
idade_hoje = data_atual.year - ano_nascimento  # Calcula a idade do usuário
print(f"{nome} tem {idade_hoje} anos de idade, {altura} de altura, pesa {peso}kg e tem o imc de {imc:.2f} ")  # renato tem 26 anos de idade, 1.8 de altura, pesa 88kg e tem o imc de 23.16
print(f"{nome} nasceu em {ano_nascimento}")  # renato nasceu em 1995

"""
renato mota tem 27 anos de idade, 1.8 de altura, pesa 88kg e tem o imc de 27.16 
renato mota nasceu em 1995
"""