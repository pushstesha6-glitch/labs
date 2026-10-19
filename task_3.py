summa=int(input("Введите сумму в рублях: "))
amount100= summa//100
summa%=100
amount50= summa//50
summa%=50
amount10= summa//10
summa%=10
amount5= summa//5
summa%=5
amount2= summa//2
summa%=2
amount1= summa//1
summa%=1
print(f"Кол-во купюр по 100 руб.: {amount100}\n"
      f"Кол-во купюр по 50 руб.: {amount50}\n"
      f"Кол-во купюр по 10 руб.: {amount10}\n"
      f"Кол-во купюр по 5 руб.: {amount5}\n"
      f"Кол-во купюр по 2 руб.: {amount2}\n"
      f"Кол-во купюр по 1 руб.: {amount1}")

