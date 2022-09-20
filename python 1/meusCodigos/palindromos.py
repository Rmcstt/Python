
pi = '979797979'

def procura_palindromo(string):
    sequencia = []  # lista vazia
    for i in range(len(string)):  # percorre a string
        for j in range(len(string), i, -1):  # percorre a string de tras pafrente 
            if string[i:j] == string[i:j][::-1]:  # verifica se a string é igual a ela mesma de tras pra frente
                sequencia.append(string[i:j])  #   adiciona a string a lista
    return sequencia  # retorna a lista 

# print(procura_palindromo(pi))

def maior_palindromo_primo(string):
    palindromos = procura_palindromo(string)
    palindromos_primos = []
    for palindromo in palindromos:
        if int(palindromo) > 1:
            for i in range(2, int(palindromo)):
                if (int(palindromo) % i) == 0:
                    break
            else:
                palindromos_primos.append(int(palindromo))
    return max(palindromos_primos)

print(maior_palindromo_primo(pi))


