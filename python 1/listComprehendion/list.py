l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [variavel for variavel in l1]  # list comprehension,itera sobre a lista criando uma nova
print(ex1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

ex2 = [variavel for variavel in l1 if variavel%2==0]  # list comprehension com if
print(ex2)  # [2, 4, 6, 8]
 
ex3 = [v * 2 for v in l1]  # multiplica por 2 todos os elementos da lista
print(ex3)  # [2, 4, 6, 8, 10, 12, 14, 16, 18]

ex4 = [(v,v2) for v in l1 for v2 in range(3)]  # v é a variavel da lista l1 e v2 é a variavel do range
print(ex4)  
""" 
 [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2), (6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2), (9, 0), (9, 1), (9, 2)]
"""

l2 = ['renato','mota','costa']

ex6 = [v.replace('a','@').replace('e','3').upper() for v in l2]  # substitui a e por @ e 3 por 3 e coloca todos os caracteres em maiusculo

print(ex6) # ['REN@TO', 'MOT@', 'COST@']

tupla = {
  ('chave','valor'),
  ('chave2','valor2'),
}

ex7 = [(y,x) for x,y in tupla]  # inverte a tupla
ex7 = dict(ex7)  # converte a tupla em dicionario
print(ex7)  # {'chave': 'valor', 'chave2': 'valor2'}


l3 = list(range(100))  # cria uma lista com 100 elementos
ex8 = [v for v in l3 if v%3==0 if v%8==0]  # filtra a lista, somente os elementos que são divisiveis por 3 e 8
print(ex8)  # [0, 24, 48, 72, 96]


ex9 = [v if v % 3 == 0 else '.' for v in l3]  # substitui os elementos que não são divisiveis por 3 por '.'
print(ex9)  
ex9 = [v if v % 3 == 0 and v% 8 == 0 else '.' for v in l3]  # substitui os elementos que não são divisiveis por 3 e 8 por '.'
print(ex9)  