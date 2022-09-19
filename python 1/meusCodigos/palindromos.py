
insira_a_string = input("Insira a string: ")

def procura_palindromo(string):
    sequencia = []  # lista vazia
    for i in range(len(string)):  # percorre a string
        for j in range(len(string), i, -1):  # percorre a string de tras pafrente 
            if string[i:j] == string[i:j][::-1]:  # verifica se a string é igual a ela mesma de tras pra frente
                sequencia.append(string[i:j])  # adiciona a string a lista
    return sequencia  # retorna a lista 

print(procura_palindromo(insira_a_string))

## chupa jeff

