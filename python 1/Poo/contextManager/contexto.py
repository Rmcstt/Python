# arquivo = open('Poo/contextManager/abc.txt', 'w')
# arquivo.write('ola, mundo!')
# arquivo.close()

# maneira usada com with é melhor pois fecha o arquivo automaticamente!!

with open('Poo/contextManager/abc.txt', 'w') as arquivo:
  arquivo.write('eai, mundo!')