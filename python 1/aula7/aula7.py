from datetime import date
data_atual = date.today()


nome = "renato mota"
idade = 26
altura = 1.80
E_maior = idade > 18
ano_nascimento = 1995

peso = 88
imc = (peso / altura ** 2)
print(data_atual.year)

print(nome, "tem", idade, "anos de idade, e seu imc é de ", imc)
print(f'{nome} tem {idade} anos de idade, e seu imc é de  {imc:.2f}')
# com Fstrings
# ":.2f" = duas casas decimais depois do ponto flutuante(float)
print('{} tem {} anos de idade, e seu imc é de  {:.2f}'.format(nome, idade, imc))
# mesmo depois deste ultimo exemplo ainda prefiro o "Fstrings

"""
renato mota tem 26 anos de idade, e seu imc é de  27.160493827160494
renato mota tem 26 anos de idade, e seu imc é de  27.16
renato mota tem 26 anos de idade, e seu imc é de  27.16
"""
idade_hoje = data_atual.year - ano_nascimento
print(f"{nome} tem {idade_hoje} anos de idade, {altura} de altura, pesa {peso}kg e tem o imc de {imc:.2f} ")
print(f"{nome} nasceu em {ano_nascimento}")
