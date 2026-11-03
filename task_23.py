income_categories=["Зарплата", "Стипендия"]
expense_categories=["Жилье","Питание","Транспорт","Развлечения"]

incomes={}
expenses={}
for category in income_categories:
    answer=input(f"Доход-{category}: ")
    incomes[category]=float(answer)
for category in expense_categories:
    answer=input(f"Расход-{category}: ")
    expenses[category] = float(answer)

def analyze(inc, exp):
    tot_inc = sum(inc.values())
    tot_exp = sum(exp.values())
    bal = tot_inc - tot_exp

    print(f"Доход: {tot_inc}")
    print(f"Расход: {tot_exp}")
    print(f"Баланс: {bal}")

    if tot_exp > 0:
        for cat, val in exp.items():
            print(f"{cat}: {val} ({(val / tot_exp) * 100:.1f}%)")
    return tot_inc, bal


def get_recommendations(tot_inc, bal, exp):
    if bal < 0:
        print("Рекомендация: Сократите расходы, у вас дефицит.")
    elif bal == 0:
        print("Рекомендация: Начните откладывать хотя бы 10% доходов.")
    else:
        print(f"Рекомендация: Вы сохраняете {(bal / tot_inc) * 100:.1f}% дохода.")

    tot_exp = sum(exp.values())
    if tot_exp > 0 and exp.get("Развлечения", 0) > tot_exp * 0.2:
        print("Рекомендация: Слишком много трат на развлечения.")


def plan_major_expense(bal):
    item = input("Покупка: ")
    price = float(input("Цена: "))

    if bal <= 0:
        print("Накопить невозможно при текущем балансе.")
    else:
        print(f"Месяцев при 100% откладывании: {price / bal:.1f}")
        print(f"Месяцев при 50% откладывании: {price / (bal * 0.5):.1f}")


total_income, balance = analyze(incomes, expenses)
get_recommendations(total_income, balance, expenses)
plan_major_expense(balance)