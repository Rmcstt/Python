import json

with open('quaseCRUD/meuJson.json', 'r') as file:
  d1_json = file.read()
  d1_json = json.loads(d1_json)

for k, v in d1_json.items():
  print(k)
  for k1, v1 in v.items():
    print(k1,v1)