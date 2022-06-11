num1 = input('digite um numero: ')
num2 = input('sera somado com...')

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('error')