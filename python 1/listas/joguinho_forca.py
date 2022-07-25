secreto = 'salgado'  # palavra secreta
digitadas = []  # lista de letras ja digitadas
chances = 3  # numero de chances
print('forca, voce tera 3 chances!!!')  # printa o jogo
print()
print()
while True:  # loop infinito
    if chances <= 0:  # se o numero de chances for menor ou igual a 0
        print('voce perdeu')  
        break  # sai do loop

    letra = input('digite uma letra: ')  

    if len(letra) > 1:  # se a letra for maior que 1
        print(' ah isso nao vale, digite apenas uma letra')
        continue

    digitadas.append(letra)  # adiciona a letra na lista de letras ja digitadas

    if letra in secreto:  # se a letra digitada estiver na palavra secreta
        print(f' boa, a letra "{letra}" que voce digitou confere!!! ')
    else:
        print(f'putz, a letra "{letra}" nao confere !!! Tente outra vez')
        digitadas.pop()  # remove a letra da lista de letras ja digitadas

    secreto_temporario = ''  # cria uma variavel temporaria para a palavra secreta
    for letra_secreta in secreto:  # para cada letra da palavra secreta
        if letra_secreta in digitadas:  # se a letra da palavra secreta estiver na lista de letras ja digitadas
            secreto_temporario += letra_secreta  # adiciona a letra na variavel temporaria
        else:
            secreto_temporario += '*'  # se a letra nao estiver na lista de letras ja digitadas, adiciona um * na variavel temporaria

    if secreto_temporario == secreto:  # se a variavel temporaria for igual a palavra secreta
        print(
            f' que legal, voce advinhou a palavra, a palavra era "{secreto_temporario}"')  
        break
    else:
        print(f' a palavra secreta esta assim: "{secreto_temporario}"')

    if letra not in secreto:  # se a letra nao estiver na palavra secreta
        chances -= 1  # diminui o numero de chances

    print(f'voce ainda tem {chances} chances')
    print()
