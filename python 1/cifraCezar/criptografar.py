texto1 = input('digite o texto a ser criptografado: ')

texto1 = list(texto1)  # converte o texto em uma lista

criptografar = [chr(ord(v) + 3) for v in texto1]  # chr() converte o valor ASCII para o caracter, ord() converte o caracter para o valor ASCII

print(''.join(criptografar))
