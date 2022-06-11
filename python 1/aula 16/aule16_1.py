idu = input('digite um numero inteiro: ')

if not idu.isdigit():
    print('this is not a int number')
else:
    idu = int(idu)
    if not idu % 2 == 0:
        print(f'{idu} is not a pair')
    else:
        print(f'{idu} is a pair')

# como proposto na aula fiz de maneira reversa