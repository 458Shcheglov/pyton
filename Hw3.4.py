# def my_pov_fun(x, y):
#     try:
#         x,y = float(x), int(y)
#         if x <= 0 or y >= 0:
#             return 'Ошибка х должени быть больше нуля, а у должен быть меньше нуля'
#         else:
#             result = 1
#             for _ in range(abs(y)):
#                 result *= 1 / x
#             return f'результат возведения х в степень у: {round(result, 6)}'
#     except ValueError:
#         return "Программа работает только с числами"
# print(my_pov_fun(2, -4,))

def my_pov_fun(x, y):
    return 1 if y == 0 else my_pov_fun(x, y + 1) * 1 / x
print(my_pov_fun(2, -4,))
