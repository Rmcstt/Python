#        indices
#        0123456789......................33
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len ( frase )
contador = 0
nova_string = ''
req_do_usuario = input('qual é a letra deseja colocar em maiuscula? ')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == req_do_usuario:
        nova_string += req_do_usuario.upper()
    else :
        nova_string += letra
    contador += 1
print(nova_string)
