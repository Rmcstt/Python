nota = int(input('nota aluno: '))
comportamento = input('o aluno se comportou? ')

if nota >= 5 or comportamento == 'sim':
    print('recupração')
elif nota >= 5 and comportamento == 'sim':
    print('and')

else:
    print('dados invalidos')