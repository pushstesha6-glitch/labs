stroka=input("Введите сроку: ").strip()
if  "".join(stroka.split())=="".join(stroka.split())[::-1]:
    print("Является палиндромом")
else:
    print("Не является палиндромом")
