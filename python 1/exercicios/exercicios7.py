carrinho = []

carrinho.append(('produto1', 30))
carrinho.append(('produto2', 20))
carrinho.append(('produto3', 20))
carrinho.append(('produto4', 20))
carrinho.append(('produto5', 50))

#### minha solução
finalizarCompra = list(carrinho)  # copia a lista
finalizarCompra = [(finalizarCompra[0][1]+finalizarCompra[1][1]+finalizarCompra[2][1]+finalizarCompra[3][1]+finalizarCompra[4][1])]  # soma 

print(finalizarCompra)  # [100]

#### solução do professor
total = sum([float(y)for x,y in carrinho])  # soma os valores da lista

print(total)  # 100.0
