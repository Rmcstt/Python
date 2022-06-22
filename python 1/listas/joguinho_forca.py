secreto = 'perfume'
digitadas = []
chances = 3
print('forca, voce tera 3 chances!!!')
print()
print()
while True:
    if chances <= 0:
        print('voce perdeu')
        break

    letra = input('digite uma letra: ')

    if len(letra) > 1:
        print(' ah isso nao vale, digite apenas uma letra')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f' boa, a letra "{letra}" que voce digitou confere!!! ')
    else:
        print(f'putz, a letra "{letra}" nao confere !!! Tente outra vez')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f' que legal, voce advinhou a palavra, a palavra era {secreto_temporario}')
        break
    else:
        print(f' a palavra secreta esta assim: "{secreto_temporario}"')

    if letra not in secreto:
        chances -= 1

    print(f'voce ainda tem {chances} chances')
    print()
