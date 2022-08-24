"""
getter = obtem um valor
setter = altera um valor
"""



from produtos import Produto


p1 = Produto('camiseta', 120)
p1.desconto(10)
print(p1.nome,p1.preco)


p2 = Produto('jordan', 'R$1200')
p2.desconto(15)
print(p2.nome,p2.preco)