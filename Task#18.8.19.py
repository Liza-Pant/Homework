amount = 0
try:
    count = int(input('Сколько билетов вы хотите купить? Введите число - '))
    for i in range(1, count + 1):
        age = int(input('Введите возраст посетителя - '))
        if age < 18:
            amount += 0
        elif 18 <= age < 25:
            amount += 990
        elif age >= 25:
            amount += 1390
except ValueError:
    print('Ошибка! Кол-во билетов было введено некорректно')
else:
    if count > 3:
        print(f'Сумма к оплате - {amount * 0.9} рублей со скидкой 10%')
    else:
        print(f'Сумма к оплате - {amount} рублей')
