texto1 = input('digite o texto a ser descriptografado: ')

texto1 = list(texto1)

descriptografar = [chr(ord(v) - 3) for v in texto1]

print(''.join(descriptografar))