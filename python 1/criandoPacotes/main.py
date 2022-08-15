from vendas.calcPreco import aumento , diminuir  # importando o módulo calcPreco.aumento e calcPreco.diminuir

import vendas.formata.preco as reais  # tive que "apelidas" o modulo para que a variavel nao fosse sobreescrita


preco = 49.90

precoComAumento = aumento(preco, 15, formata = True)
print(precoComAumento)

precoComDiminuicao = diminuir(preco, 10, formata = True)
print(precoComDiminuicao)

print(reais.real(500))