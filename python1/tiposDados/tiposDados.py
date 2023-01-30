"""
Tipos de dadps
str - string "textos com aspas"
int - inteiros (positivo ou negativo)
float - real/ ponto flutuante(numero com pontos flutuantes)
bool - boleano/logico ,(true or false)
"""

print("luiz")
print("luiz", type("luiz"))  # me lembrou o typeof do JS
print("10", type("10"))  
print(10, type(10))  
print(10.5, type(10.5))  # float
print(10 == 10, type(10 == 10))  # == é o mesmo que ==
print("l" == "l", type("l" == "l"))  # == é o mesmo que ==
print("", type(""))  # string vazia

print(bool(""))  # false
print(bool([]))  # false

print('luiz', type('luiz'), bool('luiz'))  # true
print('10', type('10'), type(int('10')))  # int convertendo um numero para inteiro
print("luiz", float("10.5"))  # float convertendo um numero para float
"""
desafio
"""

print("renato", type("renato"))  # true

print(26, type(int(26)))  # true

print(1.81, type(float(1.81)))  # true

print(26 > 18, type(26 > 18))  # true
