# Задание 1
my_list = [10, 2.0, 'Hello', True]
for el in my_list:
    print(type(el))

# Задание 2
my_list1 = []
for el in range(int(input('Пожалуйста введите число '))):
    my_list1.append(el)
print(my_list1)
a = 0
for i in range(int(len(my_list1)/2)):
    my_list1[a], my_list1[a + 1] = my_list1[a + 1], my_list1[a]
    a += 2
print(my_list1)

# Задание 3
month = int(input('Пожалуйста введите номер месяца '))
my_month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
if month in my_month[:2] or month == 12:
    print('Это зима')
elif month in my_month[2:5]:
    print('Это весна')
elif month in my_month[5:8]:
    print('Это лето')
elif month in my_month[8:11]:
    print('Это осень')
else:
    print('Вы ошиблись, такого месяца не существует')

my_dict = {'Зима': (1, 2, 12), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}
for i in my_dict.keys():
    if month in my_dict[i]:
        print(i)

# Задание 4
my_string = input('Пожалуйста введите строку из нескольких слов ').split()
for index, word in enumerate(my_string, 1):
    if len(word) > 11:
        print(index, word[:10])
    else:
        print(index, word)

# Задание 5
my_list2 = [9, 8, 6, 4, 3, 1]
e = int(input('Пожалуйста введите новое число рейтинга '))
max_el = max(my_list2)
if e > max_el:
    my_list2.insert(0, e)
elif e in my_list2:
    my_list2.insert(my_list2.index(e), e)
elif e == 0:
    my_list2.append(e)
elif e < max_el:
    my_list2.insert(my_list2.index(e - 1), e)
print(my_list2)

# Задание 6
my_list3 = []
my_analysis = {}
num = int(input('Введите количество товаров '))
i = 1
while num >= i:
    my_tuple = ({'Название': input('Введите название товара '),
                 'Цена': input('Введите цену товара '),
                 'Вес': input('Введите вес товара ')})
    my_list3.append((i, my_tuple))
    i += 1
print(my_list3)
x = []
for i in my_list3:
    x.append(i[1])
for elem in x:
    for k, v in elem.items():
        if k in my_analysis:
            my_analysis[k].append(v)
        else:
            my_analysis[k] = [v]

print(my_analysis)































