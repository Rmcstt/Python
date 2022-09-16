"""
um validador matematico de cnpj faz uma copia do mesmo e usando seus digitos para o calculo ele confere com o cpf original

ja um gerador, gera a partir de um randon fazendo o mesmo processo do validador porem os digitos foram feitos a partir do calculo dos numeros que vieram do randon......... ou seja, matematicamente sao validos!!!
"""



import re  # regular expressiom onde é usado  o re.sub para remover os caracteres que nao sejam numeros (regex)
import random  # modulo usado para gerar numeros aleatorios

REGRESSIVOS = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def valida(cnpj):  # função onde é validado o cnpj
    cnpj = apenas_numeros(cnpj)

    try:
        if eh_sequencia(cnpj):
            return False
    except:
        return False

    try:
        novo_cnpj = calcula_digito(cnpj=cnpj, digito=1)  # capta o primeiro digito para calculo
        novo_cnpj = calcula_digito(cnpj=novo_cnpj, digito=2)  #capta o segundo digito para calculo
    except Exception as e:
        return False

    if novo_cnpj == cnpj:
        return True
    else:
        return False


def calcula_digito(cnpj, digito):  #função onde é calculado os digitos (parte complexa do codigo)
    if digito == 1:
        regressivos = REGRESSIVOS[1:] # [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        novo_cnpj = cnpj[:-2]
    elif digito == 2:
        regressivos = REGRESSIVOS  # [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        novo_cnpj = cnpj
    else:
        return None

    total = 0  # variavel onde é calculado o total
    for indice, regressivo in enumerate(regressivos):
        total += int(cnpj[indice]) * regressivo

    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0  # condição onde; de o digito for maior que 9, ele se torna 0

    return f'{novo_cnpj}{digito}'


def eh_sequencia(cnpj):  # função onde é validado se o cnpj é uma sequencia
    sequencia = cnpj[0] * len(cnpj)

    if sequencia == cnpj:
        return True
    else:
        return False


def apenas_numeros(cnpj):  # função onde é removido os caracteres que nao sejam numeros
    return re.sub(r'[^0-9]', '', cnpj) # (regex)


def gera():  # função onde é gerado um cnpj aleatorio
    primeiro_digito = random.randint(0, 9)
    segundo_digito = random.randint(0, 9)
    segundo_bloco = random.randint(100, 999)
    terceiro_bloco = random.randint(100, 999)
    quarto_bloco = '0001'

    # ⬆️ nessa parte de cima sao gerados os numeros bloco a bloco

    inicio_cnpj = f'{primeiro_digito}{segundo_digito}{segundo_bloco}' \
        f'{terceiro_bloco}{quarto_bloco}00'  # aqui concatenamos os blocos gerados na primeira parte

    novo_cnpj = calcula_digito(cnpj=inicio_cnpj, digito=1)  # capta o primeiro digito para calculo
    novo_cnpj = calcula_digito(cnpj=novo_cnpj, digito=2)  #capta o segundo digito para calculo

    return novo_cnpj   


def formata(cnpj):  # função onde é formatado o cnpj para ser exibido na tela
    cnpj = apenas_numeros(cnpj)
    formatado = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    return formatado
