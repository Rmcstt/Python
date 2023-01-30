"""
preciso fazer um contador
"""

contador1 = 0
contador2 = 10

while contador1 != 11 and contador2 != 0:
    print(contador1, contador2)
    contador1 += 1
    contador2 -= 1


print()
"""
resolução do professor
"""

for e, r in enumerate(range(10, 0, -1)):
    print(e, r)

# deu a mesma coisa porem feito de uma maneira totalmente diferente!!!
