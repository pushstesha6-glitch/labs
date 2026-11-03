numbers = [float(x) for x in input("Введите числа: ").split()]

repeat={}
for n in numbers:
    if n in repeat:
        repeat[n] += 1
    else:
        repeat[n] = 1

unique_list = []
repeat_list = []
for number, count in repeat.items():
    if count > 1:
        repeat_list.append(number)
    else:
        unique_list.append(number)
print(f"Уникальные числа: {unique_list}")
print(f"Повторяющиеся числа: {repeat_list}")

even=[]
odd=[]
for n in numbers:
    if n % 1 == 0:
        if n%2==0 or n==0:
            even.append(n)
        else:
            odd.append(n)
print(f"Четные числа: {even}")
print(f"Нечетные числа: {odd}")

negative=[]
for n in numbers:
    if n<0:
        negative.append(n)
print(f"Отрицательные числа: {negative}")

float_numbers = []
for n in numbers:
    if n % 1 != 0:
        float_numbers.append(n)
print(f"Числа с плавающей точкой (дробные): {float_numbers}")

summa=0
kratno5=[]
for n in numbers:
    if n%5==0:
        kratno5.append(n)
        summa+=n
print(f"Сумма всех чисел кратных 5: {kratno5}")

max=numbers[0]
min=numbers[0]
for n in numbers:
    if n>max:
        max=n
    elif n<min:
        min=n
print(f"Максимальное число: {max}")
print(f"Минимальное число: {min}")