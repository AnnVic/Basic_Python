# Задание 1
with open('text.txt', 'w', encoding='UTF-8') as file:
    try:
        while True:
            my_string = input('Введите строку ')
            file.write(my_string + '\n')
            if not my_string:
                break
    except IOError:
        print('Ошибка ввода ')

# Задание 2
with open('text2.txt', 'r', encoding='UTF-8') as file:
    content = file.readlines()
    print(f'Количество строк {len(content)}')
    for line in content:
        res = line.count(' ') + 1
        print(f'Количество слов в строке {line} равно {res}')

# Задание 3
min_salary =[]
medium_sal = []
with open('text3.txt', 'r', encoding='UTF-8') as file:
    data = file.read()
    data = data.split('\n')
    data = data[:-2]
    print(data)
    for i in data:
        i = i.split()
        if int(i[1]) < 20000:
            min_salary.append(i[0])
        medium_sal.append(i[1])
    print(f'Оклад меньше 20000 у работников {min_salary}')
    print(f'Средний оклад работника равен {sum(map(int, medium_sal)) / len(medium_sal)}')

# Задание 4
name = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_f = []
with open('text5.txt', 'r', encoding='UTF-8') as file:
    for i in file:
        i = i.split(' ', 1)
        new_f.append(name[i[0]] + ' ' + i[1])
    print(new_f)

with open('text6.txt', 'w', encoding='UTF-8') as file:
    file.writelines(new_f)

# Задание 5
with open('text7.txt', 'w', encoding='UTF-8') as file:
    numbers = input('Введите числа, разделенные пробелом ')
    file.write(numbers)
    num = numbers.split()
    print(sum(map(int, num)))

# Задание 6
import re
my_keys = []
my_values = []
with open('text8.txt', 'r', encoding='UTF-8') as file:
    text = file.readlines()
    for i in text:
        i = i.split()
        keys = i[0]
        for i in keys.split(' '):
            my_keys.append(i)
    for line in text:
        my_line = re.findall('\d+', line)
        values = sum(map(int, my_line))
        my_values.append(values)
    data = dict(zip(my_keys, my_values))
    print(data)

# Задание 7
import json
my_profit ={}
medium_profit = {}
my_list = []
with open('text9.txt', 'r', encoding='UTF-8') as file:
    for line in file.readlines():
        name, form, profit, damage = line.split()
        my_profit[name] = int(profit) - int(damage)
        if my_profit.setdefault(name) < 0:
            print('Компания работала в убыток')
        else:
            val= sum(my_profit.values()) / len(my_profit.values())
    medium_profit = {'Medium profit': round(val)}
    my_list.append(my_profit)
    my_list.append(medium_profit)
    print(my_list)

with open('text10.txt', 'w', encoding='UTF-8') as write_f:
    json.dump(my_list, write_f)



















































