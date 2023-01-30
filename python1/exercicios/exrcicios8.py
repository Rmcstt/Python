listaA = [1,2,3,4,5,6,7,8,9,10]

listaB = [1,2,3,4,5]

#### minha solução
soma = [listaA[i] + listaB[i] for i in range(len(listaB))]  # cria uma lista com a soma de cada elemento

print(soma)  # [2, 4, 6, 8, 10]

#### solução do professor (generico)

lista_soma = []
for i in range(len(listaB)):    # percorre a listaB
    lista_soma.append(listaA[i] + listaB[i])  # adiciona o elemento da listaA na lista_soma

print(lista_soma)  # [2, 4, 6, 8, 10]

### #solução do professor (pythonic)

melhorSoma = [x + y for x, y in zip(listaA, listaB)]    # cria uma lista com a soma de cada elemento
print(melhorSoma)  # [2, 4, 6, 8, 10]

# a função zip retorna um iterador e nao um gerador.
