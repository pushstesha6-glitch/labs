a=float(input("Введите число а: "))
b=float(input("Введите число b: "))
print(f" a+b = {a+b}")
print(f" a-b = {a-b}")
print(f" a*b = {a*b}")
if  b==0:
    print(f" a:b= Ошибка")
    print(f" Остаток от деления = Ошибка")

else:
    print(f" a:b = {a / b}")
    print(f" Остаток от деления={a % b}")



