string = 'o brasil é o pais do futebol,  o brasil é penta'
lista = string.split(' ')
lista2 = string.split(',')

palavra = ''
contagem = 0

for valor in lista:
    qtd_vezes = lista.count(valor)  # função count vai conar quantos elementos

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'a palavra que apareceu mais vezes foi {palavra} ({contagem}x)')