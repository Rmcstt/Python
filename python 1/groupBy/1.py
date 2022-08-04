
from copy import deepcopy  # importa copia
from itertools import groupby  # importe o groupby

alunos = [
    {
        'nome': 'pedro',
        'nota': "A"
    },
    {
        'nome': 'joao',
        'nota': "B"
    },
    {
        'nome': 'jose',
        'nota': "C"
    },
    {
        'nome': 'luiz',
        'nota': "C"
    },
    {
        'nome': 'andre',
        'nota': "B"
    },
    {
        'nome': 'eduardo',
        'nota': "A"
    },
    {
        'nome': 'leticia',
        'nota': "D"
    },
    {
        'nome': 'fabricio',
        'nota': "A"
    },
    {
        'nome': 'moises',
        'nota': "C"
    },
    {
        'nome': 'maria',
        'nota': "B"
    }
]
def ordena(item): return item['nota']  # ordena por nota
alunos.sort(key=ordena)  # ordena alunos por nota

alunosAgrupados = groupby(alunos, lambda item: item['nota'])  # agrupa alunos por nota

# for aluno in alunos:
#   print(aluno['nome'], aluno['nota'])


for agrupamento, valoresAgrupados in alunosAgrupados:
    novosValoresAgrupados = deepcopy(valoresAgrupados)  # preferi usar deepcopy do que o tee(itertools), 
    # onde eu teria que colocar: "va1, va2 = tee(valoresAgrupados)"
    print(f'\nnota: {agrupamento}')

    quantidade = len(list(novosValoresAgrupados))  # quantidade de alunos por nota
    print(f'quantidade: {quantidade}')

    for aluno in valoresAgrupados:  # imprime alunos por nota
        print(aluno['nome'])
    print()
