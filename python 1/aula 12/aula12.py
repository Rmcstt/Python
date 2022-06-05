user = input("digite o nome do usuario: ")
qtd_caracteres = len(user)  # essa funcao retorna a quantidade de caracteres

if qtd_caracteres < 6:
    print("quantidade inssuficiente de caracteres, pelo menos 6 caracteres")
else:
    print('sucessfull')