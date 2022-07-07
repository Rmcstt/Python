"""
ainda sobre desempacotamento
"""
listas = ['renato', 'mota', 'costa', 1, 2, 3, 4, 5, 6, 7, 100]

# o asterisco acaba criando outra variavel!!!      e *_ quando vc especifica os promeiros e nao quer saber do resto!!!
n1, n2, *outra_lista, ultima = listas

print(ultima)
