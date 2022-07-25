perguntas = {
  'pergunta 1':{
  'pergunta': 'quanto é 2 + 2?',
  'respostas': {'a':'1','b':'4','c':'5','d':'6',}, 
  'respostaCerta': 'b',
  },
  'pergunta 2':{
  'pergunta': 'quanto é 3 + 3?',
  'respostas': {'a':'1','b':'4','c':'5','d':'6',},
  'respostaCerta': 'd',
  },
  'pergunta 3':{
  'pergunta': 'quanto é 4 + 4?',
  'respostas': {'a':'8','b':'4','c':'5','d':'6',},
  'respostaCerta': 'a',
  }

}

print()
respostasCertas = 0  # contador de respostas certas
for pk, pv in perguntas.items():  # percorre o dicionario
  print(f'{pk}: {pv["pergunta"]}')  # imprime a pergunta

  print('Alternativas;')  
  print()
  for rk, rv in pv['respostas'].items():  # percorre o dicionario de respostas
    print(f'[{rk}]: {rv}')  # imprime as alternativas

  respostaUser = input(f'Digite a resposta para a pergunta {pk}:')  # pede a resposta do usuario
  print()
  if respostaUser == pv ['respostaCerta']:  # verifica se a resposta do usuario é a certa
    print('resposta correta')
    respostasCertas += 1  # incrementa o contador de respostas certas
    print()
  else:
    print('resposta errada')

percentualAcertos = (respostasCertas / len(perguntas)) * 100  # calcula o percentual de acertos
percentualAcertos = round(percentualAcertos, 1)  # arredonda o percentual de acertos


print(f'voce acertou {respostasCertas} respostas.')  # imprime o numero de respostas certas
print(f'obteve {percentualAcertos}% de acertos!!!')  # imprime o percentual de acertos