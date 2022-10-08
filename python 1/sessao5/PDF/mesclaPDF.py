"""
Documentação:
https://pythonhosted.org/PyPDF2/
mais exempllos de uso:
https://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/


"""

import PyPDF2
import os


caminho_dos_pdfs = '/Users/renatomota/Desktop/juntaPdf'

novo_pdf = PyPDF2.PdfFileMerger()  # cria um objeto para juntar os pdfs

for root, dirs, files in os.walk(caminho_dos_pdfs):
  for file in files:
    caminho_completo_arquivo = os.path.join(root,file)
    with open(caminho_completo_arquivo, 'rb') as pdf:
      novo_pdf.append(pdf)

with open('/Users/renatomota/Desktop/novo.pdf', 'wb') as meu_novo_pdf:
  novo_pdf.write(meu_novo_pdf)