import random

number = random.randint(1, 100)
print(f"Загаданное число: {number}")

n = int(input("Введите предположение: "))

while n != number:
  if n > number:
    print("Меньше ")
  else:
    print("Больше ")


  n = int(input("Введите предположение: "))

print("Верно")