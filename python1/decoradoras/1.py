# def falaOi():
#   print('oi')

# variavel = falaOi

# variavel()


def master(funcao):  # decorador
    def slave(*args, **kwargs):
        print('decorado')
        funcao(*args, **kwargs)
    return slave

@master  # decorador
def falaOi():  # funcao
    print('oi')

@master
def eu(msg):
  print(msg)

# falaOi = master(falaOi)  # dispensavel ao utilisar o "@"


falaOi()
eu(' me chamo renato')
