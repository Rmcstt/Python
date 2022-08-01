from itertools import zip_longest, count  # importa o zip_longest
from textwrap import fill  # importa o fill

indice = count(+1)  # cria um contador
cidades = ["sao paulo", "belo horizonte", "salvador", "taboao da serra"]
estados = ['sp', 'mg', 'ba']

cidades_estados = zip(
    indice,
    estados,
    cidades,
)

for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)  # 1 sp sao paulo, 2 mg belo horizonte, 3 ba salvador
