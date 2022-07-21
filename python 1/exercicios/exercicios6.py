def mestre(funcao, *args, **kwargs):  # *args e **kwargs são tuplas e dicionários
  return funcao(*args, **kwargs)

def falar(nome):  # nome é uma função
  return f'oi {nome}'  

def saudacao(nome, saudacao):  
  return f'{saudacao} {nome}'

executando = mestre(falar,'renato')
executando2 = mestre(saudacao,'renato', saudacao = 'bom dia')

print(executando)
print(executando2)


  
