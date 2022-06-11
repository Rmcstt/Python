"""
variaveis
"""

nome_1 = "renato"
print(nome_1)
print(nome_1, type(nome_1))

nome = "renato mota"
idade = 26
altura = 1.80
E_maior = idade > 18
peso = 88
imc = int(peso / altura ** 2)  # operador de potencia tem peso maior que a propria divisao!!!

print("nome:", nome)
print("idade:", idade)
print("altura:", altura)
print("é maior:", E_maior)

print(imc)

aspas = """40"""

print(nome, "tem", idade, "anos de idade, e seu imc é de ", imc)

print(type(aspas))  # aspas triplas ainda se considera como string!!!

"""
renato
renato <class 'str'>
nome: renato mota
idade: 26
altura: 1.8
é maior: True
27
renato mota tem 26 anos de idade, e seu imc é de  27
<class 'str'>
"""