"""
manipulando strings
* string indices
* fatiamento de srtings (inicio, fim: passo)
* funções built-in lem, abs, type, print, etc...
essas funções podem ser usadas diretamente em cada tipo.

pode conferir isso em
https://docs.python.org/3/library/stdtypes.html (tipos built-in)
https://docs.python.org/3/library/functions.html (funções built-in)
"""
# positivos  [012345678]
texto      = 'python_s2'
# negativos -[987654321]

url = 'https://google.com.br/'

print(url[:-1])
nova_string = texto[:]  # [inicio:fim:passo]
print(nova_string)

print(len(texto))

for letra in texto:
    print(letra)