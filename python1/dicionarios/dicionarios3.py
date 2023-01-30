clientes = {
  'cliente1': {
    'nome': 'renato',
    'sobrenome': 'mota',
    'idade': '26',
  },
  'cliente2': {
    'nome': 'juliana',
    'sobrenome': 'mota',
    'idade': '50',
  },
  'cliente3': {  
    'nome': 'joão',
    'sobrenome': 'costa',
    'idade': '21',
  }
  
}

for clientes_k, clientes_v in clientes.items():  # percorre os pares chave/valor do dicionario
  print(f'exibindo {clientes_k}')
  for dados_k, dados_v in clientes_v.items():  # percorre os pares chave/valor contidos no valor do 'cliente_v'
    print(f'\t{dados_k} = {dados_v}')

