password=input("Введите пароль: ")
if len(password)<16:
    print("Слишкм короткий")
elif password.isalpha() or password.isdigit():
    print("Слабый пароль")
else:
    print("Надежный пароль")
