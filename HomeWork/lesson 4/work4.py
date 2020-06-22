# Задание 1
from sys import argv
def salary_count():
    """Функция считает заработную плату."""
    hour = int(input('Выработка в часах '))
    rate = int(input('Ставка в час '))
    premium = int(input('Размер премии '))
    result = (hour * rate) + premium
    print(f'Заработная плата равна {result}')


menu = {'count' : salary_count()}
_, func, * any_var = argv
print(*any_var)

# Задание 2
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for i, el in zip(my_list, my_list[1:]) if el > i]
print(new_list)

# Задание 3
my_list = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(my_list)

# Задание 4
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for el in my_list if my_list.count(el) < 2]
print(new_list)

# Задание 5
from functools import reduce
my_list = [el for el in range(100, 1001) if el % 2 == 0]

def my_func(prev_el, el):
    return prev_el * el
print(my_list)
print(reduce(my_func, my_list))

# Задание 6
from itertools import count, cycle
for el in count(3):
    if el > 10:
        break
    else:
        print(el)

my_list = ['Hello', 'My', 'World']
i = 0
for el in cycle(my_list):
    if i >= 10:
        break
    else:
        print(el)
    i += 1

# Задание 7
import math
from itertools import count
def fact():
    for el in count(3):
        yield math.factorial(el)
i = 0
for el in fact():
    if i < 10:
        print(el)
        i += 1
    else:
        break







