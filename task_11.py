age=int(input("Введите возраст: "))
dohod=int(input("Введите доход: "))
credit=int(input("ВВедите желаемый кредит: "))
months=int(input("Введите срок кредита: "))
credit_history=input("Ваша кредитная история: ")
porychitel=input("наличие поручателя: ")
zalog=input("Наличиие залога: ")

credit_dohod=credit/months/dohod*100

print(f" соотношение кредита к доходу: {credit_dohod}")
if  credit_dohod<=30:
    print("Категория риска: низкая")
    print("Процентная ставка: 12%-14%")
    print("Одобрить")

elif 30<credit_dohod<=50:
    print("Категория риска: средний")
    print("Процентная ставка: 15%-18%")
    if credit_history == "отличная" or credit_history == "хорошая":
        print("Одобрить")
    else:
        print("Отклонить")

elif 50<credit_dohod<=70:
    print("Категория риска: высокая")
    print("Процентная ставка: 19%-23%")
    if credit_history == "отличная" or credit_history == "хорошая":
        if porychitel == "да":
            if zalog == "да":
                print("Одобрить")
            else:
                print("Отклонить")
        else:
            print("Отклонить")
    else:
        print("Отклонить")

elif credit_dohod>70:
    print("Категория риска: критическая")
    print("Процентная ставка: 24%+")
    print("Отклонить")
