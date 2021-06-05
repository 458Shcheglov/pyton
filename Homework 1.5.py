income = int(input('Введите Вашу выручку - '))
loss = int(input('Введите Ваши здержки - '))
profit = income - loss
ability = float(profit / income * 100)

if profit >= 0:
    print('Ваша прибыль составила: ', profit, 'монет')
    ability = float(profit / income * 100)
    print('Ваша рентабельность составила: ', ability, '%')
    labor = int(input('Введите количество сотрудников: '))
    labor_profit = float(profit / labor)
    print('Прибыль, в расчёте на одного сотрудника составила: ', labor_profit, 'монет')

elif profit < 0:
    print('Ваш убыток составил: ', profit, 'монет')

# revenue = float(input('Введите значение выручки - '))
# costs = float(input('Введите значение издержек - '))
# result = revenue - costs #прибыль
# if result > 0:
#     print(f'Поздравляю! Ваша компания работает с прибылью {result} !')
#     print(f'Рентабельность выручки - {result / revenue:.3f}')
#     persons = int(input('Сколько сотрудников работает в компании? - '))
#     print(f'Прибыль на одного сотрудника - {result / persons:.3f}')
# elif result < 0:
#     print(f'Вы работаете с убытком - {result}')
# else:
#     print(f'Результат работы - нулевой')