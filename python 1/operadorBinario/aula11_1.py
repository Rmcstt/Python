"""
operadores relacionais == > >= < <= !=
"""


nome = input("qual o seu nome ? ")
idade = int(input("qual a sua idade ? "))
maior_idade = 18
idade_limite = 25
if maior_idade <= idade <= idade_limite:  # metodo simplificado do "&&"
    print(f"{nome}, seu emprestimo foi liberado")
else:
    print(f"{nome}, seu emprestimo foi negado")
