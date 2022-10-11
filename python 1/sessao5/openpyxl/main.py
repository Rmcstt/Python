"""
https://openpyxl.readthedocs.io/en/stable/

"""

from random import uniform
import openpyxl

# pedidos = openpyxl.load_workbook('/Users/renatomota/Desktop/Python/python 1/sessao5/openpyxl/excel.xlsx')
# nome_planilha = pedidos.sheetnames
# planilha = pedidos[nome_planilha[0]] # acessa a primeira plamilha

"""abrir"""
#---------------------------------------------

# for linha in planilha['a1:c4']:
#   for coluna in linha:
#     print(coluna.value)
"""ler"""
#---------------------------------------------

# for linha in planilha:
  
#     print(linha[0].value, linha[1].value, linha[2].value, linha[3].value)
"""ler"""
#---------------------------------------------

# planilha['a5'] = 4
# planilha['b5'] = 1004
# planilha['c5'] = 100
# pedidos.save('/Users/renatomota/Desktop/Python/python 1/sessao5/openpyxl/excel.xlsx')
"""escrever"""
#---------------------------------------------

# for linha in range(5, 16):
#   numero_pedido = linha - 1
#   planilha.cell(linha, 1).value = numero_pedido
#   planilha.cell(linha, 2).value = 1200 + linha

#   preco = round(uniform(10,100),2)
#   planilha.cell(linha,3).value = preco

# pedidos.save('/Users/renatomota/Desktop/Python/python 1/sessao5/openpyxl/excel.xlsx')
"""escrever em looop"""
#---------------------------------------------

planilha = openpyxl.Workbook()
planilha.create_sheet('planilha1', 0)
planilha.create_sheet('planilha2', 1)

planilha1 = planilha['planilha1']
planilha2 = planilha['planilha2']

for linha in range(1, 12):
  numero_pedido = linha - 1
  planilha1.cell(linha, 1).value = numero_pedido
  planilha1.cell(linha, 2).value = 1200 + linha

  preco = round(uniform(10,100),2)
  planilha1.cell(linha,3).value = preco

for linha in range(1, 12):
  numero_pedido = linha - 1
  planilha2.cell(linha, 1).value = numero_pedido
  planilha2.cell(linha, 2).value = 1200 + linha

  preco = round(uniform(10,100),2)
  planilha2.cell(linha,3).value = preco

planilha.save('/Users/renatomota/Desktop/Python/python 1/sessao5/openpyxl/excel3.xlsx')

"""criar nova planilha"""