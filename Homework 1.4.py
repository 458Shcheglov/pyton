
# У самого у меня толком ничего не получилось, а времени убил тучу. Мои потуги я закомментировал.
# number = int(input ('Введите целое положительное число - '))
# num_1 = number % 10
# num_2 = number // 10
# num_3 = num_2 % 10
#
# while num_2 != 0:
#     num_2 = num_2 // 10
#     num_new = num_2 % 10
#     if num_1 >= num_3 and num_1 >= num_new:
#         num_max = num_1
#     elif num_3 > num_1 and num_3 >= num_new:
#         num_max = num_3
#     elif num_new > num_1 and num_new > num_3:
#         num_max = num_new
#     print('Максимальная цифра - ', num_max)

num_init = int(input('Введите целое положительное число - '))
maximum = num_init % 10
num = num_init

while num > 0:
    digit = num % 10
    if digit > maximum:
        maximum = digit

    if digit == 9:
        break
    num = num // 10
    print(num)

print(f'Наибольшая цифра в числе {num_init} равна {maximum}')