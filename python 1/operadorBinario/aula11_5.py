user = input("Nome de usuario: ")
password = input("senha do usuario: ")

user_DB = "renatomc"
password_DB = "renato1234"

if user == user_DB and password == password_DB:
    print("✅ acess sucessfull")
elif user == user_DB or password == password_DB:
    print("❓user or password it's incorrect")
else:
    print("❌ acess danied")