carrinho = []

carrinho.append(('produto1', 30))
carrinho.append(('produto2', 20))
carrinho.append(('produto3', 20))
carrinho.append(('produto4', 20))
carrinho.append(('produto5', 50))

print(carrinho)

finalizarCompra = list(carrinho)
finalizarCompra = [finalizarCompra[0][1]+finalizarCompra[1][1]+finalizarCompra[2][1]+finalizarCompra[3][1]+finalizarCompra[4][1]]

print(finalizarCompra)
