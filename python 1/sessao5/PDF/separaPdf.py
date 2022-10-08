import PyPDF2
import os


caminho_dos_pdfs = '/Users/renatomota/Desktop/juntaPdf'

with open('/Users/renatomota/Desktop/novo.pdf', 'rb') as arquivo_pdf:
  leitor = PyPDF2.PdfFileReader(arquivo_pdf)
  for pagina in range(leitor.numPages):
    escritor = PyPDF2.PdfFileWriter()
    pagina_atual = leitor.getPage(pagina)
    escritor.addPage(pagina_atual)
    with open(f'/Users/renatomota/Desktop/novo_{pagina}.pdf', 'wb') as novo_pdf:
      escritor.write(novo_pdf)
      print(f'arquivo separado')

