"""
For in em python
iterando strings com for
funçãp range(start=0, stop, step=1)
"""

texto = input('qualquer coisa: ')

# c = 0
# while c < len(texto):
#     print(texto[c])
#     c += 1

for letra in texto:  # bem mais curto em relação ao texto comentado em cima
    print(letra)

for n, letra in enumerate(texto):  # para enumerae os indices de cada letra
    print(n, letra)
