while True:
    print()
    num_1 = input("digite um numero aqui: ")
    operator = input('digite um operador: ')
    num_2 = input('digite outro numero: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('voce precisa digitar um numero!!!')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operator == '+':
        print(num_1 + num_2)
    elif operator == '-':
        print(num_1 - num_2)
    elif operator == '/':
        print(num_1 / num_2)
    elif operator == '*':
        print(num_1 * num_2)
    else:
        print('operador invalido')

    sair = input('deseja sair ? [s] para sim e [n] para nao: ')

    if sair == 's':
        break
