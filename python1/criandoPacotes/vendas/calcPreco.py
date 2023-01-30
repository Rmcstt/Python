from vendas.formata import preco  # importando o módulo formata.preco

def aumento(valor, percentual, formata = False):  # aumento é uma função que recebe um valor e um percentual e retorna o valor com o aumento
  r = valor + (valor * percentual / 100)  # r é o valor com o aumento

  if formata:  # se formata for True, retorna o valor formatado
    return preco.real(r)
  else:
    return r 


def diminuir(valor, percentual, formata = False):  # diminuir é uma função que recebe um valor e um percentual e retorna o valor com a diminuição
  r = valor - (valor * percentual / 100)  # r é o valor com a diminuição
  
  if formata:  # se formata for True, retorna o valor formatado
    return preco.real(r)
  else:
    return r


