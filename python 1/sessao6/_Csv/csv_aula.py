"""
comma separated values - csv (valores separados por virgula)
é um formato de arquivo de texto que armazena dados em forma de tabela(excel, google dheets), bases de dados, clientes de email etc.
"""

import csv


with open('/Users/renatomota/Desktop/Python/python 1/sessao5/_Csv/clientes.csv', 'r') as arquivo:
    dados = csv.DictReader(arquivo)
    for dado in dados:  # tem que estar escrito corretamente , ate mesmo os espaços !!!
        print(dado['Nome'], dado[' Sobrenome'],  dado[' email'], dado[' telefone'])
