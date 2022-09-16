"""
CPF = 168.995.350-09
-----------------------------------------------------------
1 * 10 = 10                 #     1 * 11 = 11 <-
6 * 9  = 54                 #     6 * 10 = 60
8 * 8  = 64                 #     8 *  9 = 72
9 * 7  = 63                 #     9 *  8 = 72
9 * 6  = 54                 #     9 *  7 = 63
5 * 5  = 25                 #     5 *  6 = 30
3 * 4  = 12                 #     3 *  5 = 15
5 * 3  = 15                 #     5 *  4 = 20
0 * 2  = 0                  #     0 *  3 = 0
                            #  -> 0 *  2 = 0
         297                #              343 
11 - (297 % 11) = 11        #    11 - (343 % 11) = 9
11 > 9 = 0                  #    
digito 1 = 0                #    digito 2 = 9
"""

while True:
    cpf = input(' digite seu CPF:')
    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0

    for index in range(19):  # multiplicando os numeros do cpf por suas posições 
        if index > 8:  
            index -= 9  # subtraindo 9 para nao ultrapassar o tamanho do cpf

        total += int(novo_cpf[index]) * reverso  # somando os numeros multiplicados

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)  # calculando o digito verificador

            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)

    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)

    if cpf == novo_cpf and not sequencia:
        print(f'CPF: {cpf} Válido')
    else:
        print(f'CPF: {cpf} Inválido')
