"""..."""

variavel_1 = 'valor'

def soma(x,y):
    """Soma dois numeros"""
    return x+y

def multiplica(x,y, z=None):
    """Multiplica dois numeros
    o programador pode passar um terceiro argumento opcional
    """
    if z:
      return x*y*z
    return x*y


print(multiplica(2,3,3))

valor2 = 'valor 2'
valor3 = 'valor 3'
valor4 = 'valor 4'
