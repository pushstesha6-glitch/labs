sales=[
    {"name": "Шоколад", "price": 7, "amount": 15},
    {"name": "Батончик", "price": 3, "amount": 9},
    {"name": "Мармеладки", "price": 4, "amount": 12},
    {"name": "Чипсы", "price": 4, "amount": 10},
    {"name": "Сухарики", "price": 2, "amount": 17},
]

total_sales={}
for product in sales:
    name=product["name"]
    price=product["price"]*product["amount"]
    if name in total_sales:
        total_sales[name]+=price
    else:
        total_sales[name]=price
print(f"Вырочка за каждый продукт: {total_sales}")

max_sale = max(total_sales, key=total_sales.get)

print(f"Самый прибыльный товар: {max_sale} , выручка: {total_sales[max_sale]})")