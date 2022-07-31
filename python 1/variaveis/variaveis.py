"""
variaveis
"""

nome_1 = "renato"  # string
print(nome_1)  # renato
print(nome_1, type(nome_1))  # renato <class 'str'>

nome = "renato mota"
idade = 26
altura = 1.80
E_maior = idade > 18
peso = 88
imc = int(peso / altura ** 2)  # operador de potencia tem peso maior que a propria divisao!!!

print("nome:", nome)  # nome: renato mota
print("idade:", idade)  # idade: 26
print("altura:", altura)  # altura: 1.8
print("é maior:", E_maior)  # é maior: True

print(imc)  # 23

aspas = """40"""  # string com multiplas linhas

print(nome, "tem", idade, "anos de idade, e seu imc é de ", imc)  # renato tem 26 anos de idade, e seu imc é de 23

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