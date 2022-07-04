string = 'o brasil é o pais do futebol,  o brasil é penta'
lista = string.split ( ' ' )
lista2 = string.split ( ',' )

for valor in lista2 :
    print ( valor.strip ().capitalize () )  # função strip serve para eliminar paragrafros

    # função captalize deixa a primeira letra maiuscula, ao contrario da Upper que deixa todas as letras
