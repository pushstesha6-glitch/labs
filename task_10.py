summa=int(input("Введите сумму покупки: "))
age=int(input("ВВедите возраст: "))
birthday=int(input("Введите день и месяц рождения: "))
data=int(input("Введите сегодняшний день и месяц: "))
vip=input("Вы вип клиент?: ")

discount=0
if vip == "да":
    discount = 15
elif summa > 1000:
    discount = 10

if age>=63:
    discount=discount+5
if birthday==data:
        discount=discount+5

if discount > 25:
    discount = 25

summa=summa-summa*discount/100
print(f"Итоговая сумма со скидками: {summa}")



