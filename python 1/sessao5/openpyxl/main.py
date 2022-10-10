"""
https://openpyxl.readthedocs.io/en/stable/

"""

import openpyxl

pedidos = openpyxl.load_workbook('/Users/renatomota/Desktop/Python/python 1/sessao5/openpyxl/excel.xlsx')
nome_planilha = pedidos.sheetnames
planilha = pedidos[nome_planilha[0]] # acessa a primeira plamilha

#---------------------------------------------

# for linha in planilha['a1:c4']:
#   for coluna in linha:
#     print(coluna.value)

#---------------------------------------------

# for linha in planilha:
  
#     print(linha[0].value, linha[1].value, linha[2].value, linha[3].value)

#---------------------------------------------

planilha['a5'] = 4
planilha['b5'] = 1004
planilha['c5'] = 100
pedidos.save('/Users/renatomota/Desktop/Python/python 1/sessao5/openpyxl/excel.xlsx')