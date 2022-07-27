"""
separar numeros
"""



string = '01234567890123456789012345678901234567890123456789012345678901234567890123456789'

l1 = [string[i:i + 10] for i in range(0, len(string), 10)]  # separa os numeros em grupos de 10

l2 = '.'.join(l1)  # join list with '.'

print(l1)  
print(l2)  

numeros = [[numero, numero** 2 ] for numero in range(11)]  # cria uma lista de listas, onde é composta por um numero e seu quadeado!!!
print(numeros)

flat = [y for x in numeros for y in x]  # desacolha a lista de listas
print(flat)
