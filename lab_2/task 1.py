money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
b = money_capital+salary-spend # бюджет 1 месяц
count = 2 #1 месяц посчитан начинаем со 2ого
while spend<=b:
    count+=1
    spend+=increase*spend
    b+=salary-spend
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", count)
