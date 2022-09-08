class Pai:
  nome = 'teste'


A = type('A', (), {'attr' : ' ola mundo'})
# ate mesmo o type é um objeto quando instanciado...

a = A()
print(a.attr)
