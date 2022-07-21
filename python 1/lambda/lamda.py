def funcao(arg1, arg2):  # arg1 e arg2 são variaveis!!!
  return arg1 * arg2



print(funcao(2,3))  # 6


a = lambda arg3, arg4: arg3 * arg4  # lamba é uma funcao anonima!!!

print(a(2,3))  # 6


lista = [
  ['p1', 13],
  ['p2', 6],
  ['p3', 7],
  ['p4', 50],
  ['p5', 1],
]

# def func(item):
#   return item[1]

# lista.sort(key=func, reverse= True)


#####

# lista.sort(key=lambda item: item[1], reverse= True)  
# print(lista)
print(lista)
print(sorted(lista, key=lambda item: item[1], reverse= True))  # ordena a lista por ordem decrescente