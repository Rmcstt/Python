num1 = input('digite um numero: ')
num2 = input('sera somado com...')

try:  # tenta executar o codigo abaixo
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:  # se der erro, executa o codigo abaixo
    print('error')