import PyPDF2
import os


caminho_dos_pdfs = '/Users/renatomota/Desktop/juntaPdf'

with open('/Users/renatomota/Desktop/novo.pdf', 'rb') as arquivo_pdf:
  leitor = PyPDF2.PdfFileReader(arquivo_pdf)  # cria um objeto para ler o pdf
  for pagina in range(leitor.numPages):
    escritor = PyPDF2.PdfFileWriter()  # cria um objeto para escrever o pdf
    pagina_atual = leitor.getPage(pagina)
    escritor.addPage(pagina_atual)  # adiciona a página atual ao novo pdf
    with open(f'/Users/renatomota/Desktop/novo_{pagina}.pdf', 'wb') as novo_pdf:
      escritor.write(novo_pdf)  # escreve o novo pdf
      print(f'arquivo separado')

