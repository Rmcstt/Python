import json

d1 = {
  'pessoa 1': {
    'nome': 'joao',
    'idade': 20,
  },
  'pessoa 2': {
    'nome': 'maria',
    'idade': 21,
  }
}

d1_json = json.dumps(d1, indent=True)

with open('quaseCRUD/meuJson.json', 'w+') as file:
  file.write(d1_json)
print(d1_json)