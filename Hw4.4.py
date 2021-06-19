from random import randint

my_list = [randint(-10, 10) for _ in range(20)]
uniq_lst = [el for el in my_list if my_list.count(el) ==1]
print(f'Начальный сисок\n{my_list}\nСписок без повторений\n{uniq_lst}')


print(a := [randint(0, 9) for j in range(20)], '\n', [i for i in a if a.count(i) == 1], sep="")
