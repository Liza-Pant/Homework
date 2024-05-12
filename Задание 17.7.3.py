per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму,которую планируете положить под проценты:'))
deposit = list(per_cent.values())
for i in range(len(deposit)):
    deposit[i] = deposit[i] * money*0.01
print('Депозит составит:', deposit)

max_deposit= max(deposit)
print('Максимальная сумма, которую вы можете заработать — ', max_deposit, 'рублей')