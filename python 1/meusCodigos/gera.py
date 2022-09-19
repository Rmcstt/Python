import os

cpf = input('digite o cpf: ')

n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11 = cpf
m1 = int(n1) * 10
m2 = int(n2) * 9
m3 = int(n3) * 8
m4 = int(n4) * 7
m5 = int(n5) * 6
m6 = int(n6) * 5
m7 = int(n7) * 4
m8 = int(n8) * 3
m9 = int(n9) * 2

soma1 = m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8 + m9

mm1 = int(n1) * 11
mm2 = int(n2) * 10
mm3 = int(n3) * 9
mm4 = int(n4) * 8
mm5 = int(n5) * 7
mm6 = int(n6) * 6
mm7 = int(n7) * 5
mm8 = int(n8) * 4
mm9 = int(n9) * 3
mm10 = int(n10) * 2

soma2 = mm1 + mm2 + mm3 + mm4 + mm5 + mm6 + mm7 + mm8 + mm9 + mm10

if soma1 % 11 == 0 or soma1 % 11 == 1:
    digito1 = 0
else:
    digito1 = 11 - (soma1 % 11)

if soma2 % 11 == 0 or soma2 % 11 == 1:
    digito2 = 0

else:
    digito2 = 11 - (soma2 % 11)

sequencia = n1 == n2 == n3 == n4 == n5 == n6 == n7 == n8 == n9 == n10 == n11

if digito1 == int(n10) and digito2 == int(n11) and not sequencia:
    print('cpf valido')

else:
    print('cpf invalido')



