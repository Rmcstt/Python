from produtos import pessoas, produtos, lista  # importação de produtos.py

novaLista = filter(lambda x: x >5,lista)  # filtra a lista com a função lambda e passa o parametro
print(list(novaLista))  # [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

nova_lista = [x for x in lista if x > 5]  # list comprehension - forma mais facil de fazer o filter
print(nova_lista)  # [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

novosProdutos = filter(lambda p : p ['price'] > 1000, produtos)  # filtra os produtos com a função lambda e passa o parametro

for produto in novosProdutos:  # percorre o gerador
  print(produto)  # imprime os produtos com preço maior que 1000

print()

def filtraPreco(produto):  # função para filtrar os produtos com preço maior que 1000
  if produto['price'] > 1000:  # se o preço for maior que 1000
    return True  # retorna True

novos_produtos = filter(filtraPreco, produtos)  # chamo a função filtraPreco para cada produto da lista

for new_produto in novos_produtos:  # percorre o gerador
  print(new_produto)

def filtraIdade(pessoa):  # função para filtrar as pessoas maiores de idade
  if pessoa['idade'] >= 18:  # se a idade for maior ou igual a 18
    return True
 

novasIdades = filter(filtraIdade, pessoas)  # chamo a função filtraIdade para cada pessoa da lista

for novaIdade in novasIdades:  # percorre o gerador
  print(novaIdade)  # imprime as pessoas maiores de idade

