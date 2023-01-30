listas = [
    ['renato', 'mota', 'costa'],
    ['habigail', 'emidio', 'martins'],
    ['luna', 'emidio', 'mota']
]

print(listas[2][2])  # como se fosse um eixo x e y , ou ate mesmo um plano cartesiano!!!
print(listas[1][0])  # primeiro lista mae e depois lista filha!!!

enumerada = enumerate(listas)

print(enumerada)  # <enumerate object at 0x10c20b400>  "WTF"

print(list(enumerada))
# [
# (0, ['renato', 'mota', 'costa']),
# (1, ['habigail', 'emidio', 'martins']),
# (2, ['luna', 'emidio', 'mota'])
# ]

print(listas[2][0],listas[1][1],listas[0][1])  # s2

for indice, valor in enumerate(listas, 21):
    print(indice, valor)

    # 21['renato', 'mota', 'costa']
    # 22['habigail', 'emidio', 'martins']
    # 23['luna', 'emidio', 'mota']

  # manipular listas = manipular array
