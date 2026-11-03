set1 = set(float(x) for x in input("Введите первый набор чисел: ").split())
set2 = set(float(x) for x in input("Введите второй набор чисел: ").split())

common = set1.intersection(set2)
print(f"Числа в обоих наборах: {list(common)}")

only_first = set1.difference(set2)
only_second = set2.difference(set1)
print(f"Только в первом наборе: {list(only_first)}")
print(f"Только во втором наборе: {list(only_second)}")

all=set1.union(set2)
exclusive=all.difference(common)
print(f" Числа из обоих наборов, за исключением чисел, найденных в пункте 1: {list(exclusive)}")