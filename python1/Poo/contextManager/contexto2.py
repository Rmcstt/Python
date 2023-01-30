
# gerenciador de contexto serve para abrir e fechar arquivos, conexoes,etc...

class Arquivo:
  def __init__(self, arquivo, modo):
    print('INIT')
    self.arquivo = open(arquivo, modo)

  def __enter__(self):
    print('entrou na classe')
    return self.arquivo


  def __exit__(self, exc_type, exc_val, exc_tb):
    print('saiu da classe')
    # tratamento de erros
    self.arquivo.close()

with Arquivo('Poo/contextManager/abc.txt', 'w') as arquivo:
  arquivo.write('fala, mundo')