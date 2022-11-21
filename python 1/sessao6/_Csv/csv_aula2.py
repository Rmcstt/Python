import csv

with open('/Users/renatomota/Desktop/Python/python 1/sessao5/_Csv/clientes.csv', 'r') as arquivo:
  dados = [x for x in csv.DictReader(arquivo)]

with open('/Users/renatomota/Desktop/Python/python 1/sessao5/_Csv/clientes2.csv', 'w') as arquivo:
  escreve = csv.writer(
    arquivo,
    delimiter=',',
    quotechar='"',
    quoting=csv.QUOTE_ALL


  )

  chaves = dados[0].keys()
  chaves = list(chaves)
  escreve.writerow(
    [
      chaves[0],
      chaves[1],
      chaves[2],
      chaves[3],
    ]


  )

  for dado in dados:
    escreve.writerow(
      [
        dado['Nome'],
        dado['Sobrenome'],
        dado['email'],
        dado['telefone']
      ]
    )