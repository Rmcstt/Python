# tudo em python é objeto

"""
str - string
"""
print('aspas simples')
print("aspas duplas")
print(1234)

print(1 + 1)
print("1" + "1")  # parecido com JS

print("essa é uma 'string' (str).")  # ✅
print('essa é uma "string" (str).')  # ✅
print("essa é uma \"string\" (str).")  # ❌
print('essa é uma \'string\' (str).')  # ❌
print('essa é uma \nstring\' (str).')  # ❌ \n quebra a linha
print(r'essa é uma \nstring\' (str).')  # ❌ "r" antes da string pede pra nao executar nada dentro do texto

# aspas simples
# aspas duplas
# 1234
# 2
# 11
# essa é uma 'string' (str).
# essa é uma "string" (str).
# essa é uma "string" (str).
# essa é uma 'string' (str).
# essa é uma
# string' (str).
# essa é uma \nstring\' (str).
