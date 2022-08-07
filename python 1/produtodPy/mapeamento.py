
from produtos import pessoas, produtos, lista  # importação de produtos.py

novaLista = map(lambda x: x * 2, lista)
# o map ira pegar a lista original com a função lambda e multiplicar por 2, passando a lista como parametro
novaLista2 = [x * 2 for x in lista]
# list comprehension - forma mais facil de fazer o map
print(lista)  # lista original
print(list(novaLista))  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] o map nao converte diretamente para lista, po isso isei o list()
print(novaLista2)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20].

########################################################################################################################

def desconto(p):  # função para calcular o desconto
  p['price'] = round(p['price'] * 0.9,2)  # calcula o desconto e arredonda para 2 casas decimais
  return p  # retorna o produto com o desconto..

novosPrecos = map(desconto, produtos)  # com o map eu chamo a função desconto para cada produto da lista
soPreco = map(lambda x: x['price'], novosPrecos)  # com esse outro map eu pego apenas os produtos da lista


for preco in soPreco:  #... para cada preco da lista de precos...
  print(preco)  #improme apenas os precos com desconto

########################################################################################################################

soNome = map(lambda n: n['nome'], pessoas)

for nome in soNome:
  print(f'\n{nome}')




