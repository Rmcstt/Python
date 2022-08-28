from classes import CarrinhoDeCompras,Produto

carrinho = CarrinhoDeCompras()  #instanciando a classe carrinho
p1 = Produto('camiseta', 49.90)  # instanciando os produtos
p2 = Produto('tenis', 299.90)
p3 = Produto('calça', 119.90)

carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)

carrinho.lista_produtos()
print(carrinho.soma_total())