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
print(10.5, type(10.5))
print(10 == 10, type(10 == 10))
print("l" == "l", type("l" == "l"))
print("", type(""))

print(bool(""))
print(bool([]))

print('luiz', type('luiz'), bool('luiz'))
print('10', type('10'), type(int('10')))  # int convertendo um numero para inteiro
print("luiz", float("10.5"))
"""
desafio
"""

print("renato", type("renato"))

print(26, type(int(26)))

print(1.81, type(float(1.81)))

print(26 > 18, type(26 > 18))

"""
luiz
luiz <class 'str'>
10 <class 'str'>
10 <class 'int'>
10.5 <class 'float'>
True <class 'bool'>
True <class 'bool'>
 <class 'str'>
False
False
luiz <class 'str'> True
10 <class 'str'> <class 'int'>
luiz 10.5
renato <class 'str'>
26 <class 'int'>
1.81 <class 'float'>
True <class 'bool'>
"""
