horario = input('digite o horario atual: ')

if horario.isdigit():  # isdigit() verifica se o valor é um numero
    horario = int(horario)
    if horario < 0 or horario > 23:
        print('o horario deve estar entre 0 e 23')
    else:
        if horario <= 11 :
            print('bom dia')
        elif horario <= 17:  #elif é um else if
            print('boa tarde')
        else:
            print('boa noite')

else:
    print('por favor digite um horario entre 0 e 23 horas')