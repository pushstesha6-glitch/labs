phone=60
sms=30
internet=1024
summa=24.99
dop_min=0.89
dop_sms=0.59
dop_mb=0.79

user_phone=int(input("Израсходованное кол-во минут: "))
user_sms=int(input("Кол-во смс-сообщений: "))
user_internet=int(input("Израсходованные мб интернет-трафика: "))
print(f"Базовая сумма тарификации: {summa}")

total=summa
if user_phone>phone:
    print(f"Базовая сумма за доп минуту: {dop_min}")
    user_dop_min=dop_min*(user_phone-phone)
    print(f"Итоговая сумма за доп минуты: {user_dop_min:.2f}")
    total+=user_dop_min
if user_sms>sms:
    print(f"Базовая сумма за доп смс: {dop_sms}")
    user_dop_sms=dop_sms*(user_sms-sms)
    print(f"Итоговая сумма за доп смс: {user_dop_sms:.2f}")
    total+=user_dop_sms
if user_internet>internet:
    print(f"Базовая сумма за доп мб: {dop_mb}")
    user_dop_internet=dop_mb*(user_internet-internet)
    print(f"Итоговая сумма за интернет: {user_dop_internet:.2f}")
    total+=user_dop_internet
tax = total * 0.02
print(f"Налог: {tax:.2f}")
total=total+tax
print(f"Итговая сумма за месяц: {total:.2f}")




