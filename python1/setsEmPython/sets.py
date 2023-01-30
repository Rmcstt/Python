"""
add (adiciona), update(atualiza), clear(limpa), remove(remove), discard(remove), pop(remove e retorna o elemento)
union "|"(uniao), intersection(interseccao), difference(diferenca, elementos apenas no set da esquerda), symmetric_difference(diferenca simetrica)
issubset(subconjunto), issuperset(superconjunto), issuperset(subconjunto), issuperset(superconjunto)
"""


s1 = {1, 2, 3, 4, 5}  # cria o set s1
# nao da para acessar diretamente, mas da para iterar com "for"
print(s1)

s2 = set()
s2.add(1)  # adiciona 1 ao set s2
s2.add(2)
s2.add(3)
# adiciona mais de um elemento, precisa estar dentro de umma tupla.
s2.add(('renato', 'mota'))
# {('renato', 'mota'), 1, 2, 3} ou {1, 2, 3, ('renato', 'mota')}, anomalia no python 🤷🏻‍♂️
print(s2)

s2.discard(2)  # remove o elemento 2 do set s2
print(s2)  # {('renato', 'mota'), 1, 3} ou {1, 3, ('renato', 'mota')}

s2.clear()  # limpa o set s2

s2.update('renato')
# {'o', 'a', 't', 'e', 'r', 'n'} ele itera sobre o elemento 'renato' porem de forma embaralhada 🤷🏻‍♂️
print(s2)

s2.clear()

s2.update([1, 2, 3, 4, 5], {5, 6, 7, 8, 9})
print(s2)  # {1, 2, 3, 4, 5, 6, 7, 8, 9} nao repete elementos.

"""
listas para set
"""

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'renato', 'mota']
s3 = set(l1)  # cria o set s3 com os elementos da lista l1
print(s3)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'renato', 'mota'}

s3.remove('renato')  # remove o elemento 'renato' do set s3
l2 = list(s3)  # cria a lista l2 com os elementos do set s3

print(l2)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'mota']


"""
manipulando conjuntos
"""

ss1 = {1, 2, 3, 4, 5}  # cria o set ss1
ss2 = {4, 5, 6, 7, 8, 9}  # cria o set ss2


# uniao
ss3 = ss1 | ss2  # uniao de ss1 e ss2
print(ss3)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# interseccao
ss4 = ss1 & ss2  # interseccao de ss1 e ss2
print(ss4)  # {4,5}

# diferenca
ss5 = ss1 - ss2  # diferenca de ss1 e ss2
print(ss5)  # {1, 2, 3} apenas os elementos da esquerda

# diferenca simetrica
ss6 = ss1 ^ ss2  # diferenca simetrica de ss1 e ss2
print(ss6)  # {1, 2, 3, 6, 7, 8, 9}

# subconjunto
print(ss1 <= ss3)  # Ttrue

# superconjunto
print(ss3 >= ss1)  # Ttrue

