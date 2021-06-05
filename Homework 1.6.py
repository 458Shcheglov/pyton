while True:
    days = 1
    start_km = float(input('Начальный результат - '))
    last_km = float(input('Финальный результат - '))
    if start_km <= 0 or last_km < 0:
        print('Результаты должны быть больше нуля. Стартовое значение != 0')
    else:
        while start_km < last_km:
            start_km *= 1.1
            days += 1
        print(f'Спортсмен добъётся результата за {days} дней')

# import math
# start_km = 2
# last_km = 6
# print(math.ceil(math.log(last_km / start_km, 1.1)) + 1)

