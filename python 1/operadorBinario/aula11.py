"""
condições IF, ELIF e ELSE
"""
# ao contrario de JS, o python usa "elif" ao invez de "else if", fora que nao tem as chaves !!!

num = int(input("tenta a sorte "))
if num % 2 == 0:
    print("divisivel por 2")
elif num % 3 == 0:
    print("divisivel por 3")
elif num % 4 == 0:
    print("divisivel por 4")
elif num % 5 == 0:
    print("divisivel por 5")
elif num % 6 == 0:
    print("divisivel por 6")
elif num % 7 == 0:
    print("divisivel por 7")
elif num % 8 == 0:
    print("divisivel por 8")
elif num % 9 == 0:
    print("divisivel por 9")
else:
    print("divisivel por ele mesmo")
