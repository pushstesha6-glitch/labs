category=input("Введите тип измерения: ")
unit_before=input("Введите исходную  единицу: ")
unit_after=input("Введите целевую единицу: ")
value=float(input("Введите значение: "))

if category=="длина":
    if unit_before=="см":
        if unit_after=="м":
            print(f"{value} {unit_before}  = {value/100} {unit_after}")
        elif unit_after=="мм":
            print(f"{value} {unit_before}  = {value*10} {unit_after}")
    elif unit_before=="м":
            if unit_after=="км":
                print(f"{value} {unit_before}  = {value/1000} {unit_after}")
            elif unit_after=="см":
                 print(f"{value} {unit_before}  = {value*100} {unit_after}")

elif category=="вес":
    if unit_before=="кг":
        if unit_after=="г":
            print(f"{value} {unit_before}  = {value*1000} {unit_after}")
        if unit_after=="т":
            print(f"{value} {unit_before}  = {value/1000} {unit_after}")

elif category=="время":
    if unit_before=="с":
        if unit_after=="мин":
            print(f"{value} {unit_before}  = {value/60} {unit_after}")
        if unit_after=="ч":
            print(f"{value} {unit_before}  = {value/3600} {unit_after}")
    if unit_before=="мин":
        if unit_after=="с":
            print(f"{value} {unit_before}  = {value*60} {unit_after}")
        if unit_after=="ч":
            print(f"{value} {unit_before}  = {value/60} {unit_after}")

else :
    print("Такой величины измерения нет ")