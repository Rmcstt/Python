# gerador

from random import randint
numero = str(randint(100000000, 999999999))

novo_cpf1 = numero
reverso = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9

    total += int(novo_cpf1[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        novo_cpf1 += str(d)

# validador

novo_cpf2 = novo_cpf1[:-2]
reverso2 = 10
total2 = 0

for index2 in range(19):
    if index2 > 8:
        index2 -= 9

    total2 += int(novo_cpf2[index2]) * reverso2

    reverso2 -= 1
    if reverso2 < 2:
        reverso2 = 11
        d2 = 11 - (total2 % 11)

        if d2 > 9:
            d2 = 0
        total2 = 0
        novo_cpf2 += str(d2)


if novo_cpf1 == novo_cpf2:
    print(f'CPF: {novo_cpf1} Válido')
else:
    print(f'CPF: {novo_cpf1} Inválido')
