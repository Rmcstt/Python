# problema dos parametros mutaveis.


# mutaveis; listas, dicionarios
# nao mutaveis; tuplas, strings, numeros, True, False, None, ... 

##################

# def listaClientes(clientesIteraveis, lista=[])
# lista.extend(clientesIteraveis)
#   return lista


# clientes1 = listaClientes(['João', 'Maria', 'Pedro'])
# clientes2 = listaClientes(['marcio','junior','ana'])
# clientes1 = listaClientes(['josue'])
# print(clientes1)  # ❌ ele juntou os dois clientes em uma lista
# print(clientes2)  # ❌ ele juntou os dois clientes em uma lista

##################

def listaClientes(clientesIteraveis, lista=None):  # troquei "[]" por none para que nao seja criada uma nova lista.
  if lista is None:  # maneira para evitar o erro de mutabilidade 
    lista = []
  lista.extend(clientesIteraveis)
  return lista


clientes1 = listaClientes(['João', 'Maria', 'Pedro'])
clientes2 = listaClientes(['marcio','junior','ana'])
clientes3 = listaClientes(['josue'])

print(clientes1)  # ✅ cada cliente tera sua propria lista
print(clientes2)  # ✅ cada cliente tera sua propria lista
print(clientes3)  # ✅ cada cliente tera sua propria lista