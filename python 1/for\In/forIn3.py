texto = 'Python'
nova_string = ''

for letra in texto:  # para e onde
    if letra == 'p':
        nova_string += letra.upper()
    elif letra == 't':
        nova_string += letra.upper()
    else:
        nova_string += letra
print(nova_string)