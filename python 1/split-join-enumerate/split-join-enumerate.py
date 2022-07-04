"""
split - join - enumerate em python
* split = dividir uma string # str
* join = juntar uma lista # str
* enumerate = enumerar ellementos de uma lista # list (objetos iteraveis)
"""

string = 'o brasil é o pais do futebol,  o brasil é penta'
lista = string.split(' ')
lista2 = string.split(',')

print(lista2)

for valor in lista:
    print(f'a palavra {valor} apareceu {lista.count(valor)}x na frase')