"""
public, protected, private

public: pode ser acessado de qualquer lugar
protected: pode ser acessado apenas dentro da classe e nas classes filhas
private: pode ser acessado apenas dentro da classe

🛑 esses metodos nao existem em python, mas podemos simular com ;

_ -> protected '_nome'
__ -> private '__nome'


"""

class baseDeDados:  # classe base
  def __init__(self):  # metodo contrutor
    self.__dados = {}  # dicionario privado

  @property  # getter
  def dados(self):  # getter
    return self.__dados  # retorna o dicionario 

  def inserir_cliente(self, id, nome):
    if 'clientes' not in self.__dados:
      self.__dados['clientes'] = {id: nome}  # cria o dicionario
    else:
      self.__dados['clientes'].update({id: nome})  # atualiza

  def lista_clientes(self):  # for na lista de clientes
    for id, nome in self.__dados['clientes'].items():
      print(id, nome)

  def apaga_cliente(self, id):  # apaga o cliente
    del self.__dados['clientes'][id]

bd = baseDeDados()

bd.inserir_cliente(1, 'renato')
bd.inserir_cliente(2, 'joao')
bd.inserir_cliente(3, 'maria')
bd.inserir_cliente(4, 'birobiro')

bd.apaga_cliente(3)

bd.lista_clientes()

print(bd._baseDeDados__dados)  # acessando atributo privado
print(bd.dados)  # somente leitura (@property, getter)



