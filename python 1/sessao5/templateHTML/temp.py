from string import Template
from datetime import datetime
import random



lista = ['joao','maria', 'pedro', 'jose', 'marcos', 'ana', 'carlos', 'julia', 'josefa', 'josefina']

sorteio = random.choice(lista)










#----------------------------------------------#

with open('/Users/renatomota/Desktop/Python/python 1/sessao5/templateHTML/template.html', 'r') as html:
  template = Template(html.read())
  data_atual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
  corpo_msg = template.safe_substitute(nome=sorteio,data=data_atual)

print(corpo_msg)
print(sorteio)