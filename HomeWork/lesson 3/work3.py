# Задание 1
def num_division(a, b):
    """Возвращает результат деления 2 чисел.
    #:param a: int
    #:param b: int
    #:return: float
    #"""
    try:
        a / b
        return a / b
    except ZeroDivisionError as e:
        print(e)

num = int(input('Введите делитель '))
num2 = int(input('Введите делимое '))
print(num_division(num, num2))

# Задание 2
def user_data(name, surname, year, city, email, phone):
    """Выводит данные пользователя одной строкой"""
    print(f'{name} {surname} {year} года рождения проживает в городе {city}, контактные данные:{email}, телефон {phone}.')

user_data(name='John', surname='Smith', year=1990, city='London', email='john@gmail.com', phone=373907685)

# Задание 3
def my_func(a, b, c):
    """Функция принимает 3 аргумента и возвращает сумму 2 наибольших"""
    my_list = [a, b, c]
    num = min(my_list)
    my_list.remove(num)
    return sum(my_list)
print(my_func(20, 100, 600))

# Задание 4
def my_func(x, y):
    """Функция возводит число в степень"""
    return x ** y
print(my_func(2, -6))

def my_func1(x, y):
    """Функция возводит число в степень"""
    result = 1
    for i in range(abs(y)):
        result *= x
    if y >= 0:
        return result
    else:
        return 1 / result
print(my_func1(2, -6))

# Задание 5
# Программа выводит сумму чисел
a = 0
while True:
    try:
        number = input('Введите числа, разделенные пробелом или q для выхода ').split()
        for n in map(int, number):
            a += n
        print(a)
    except ValueError as error:
        for i in number:
            if 'q' in i:
                print('Выход')
        break

# Задание 6
int_func = lambda x: x.capitalize()
print(int_func('name'))

def my_func1(x):
    """Функция принимает строку и возвращает каждое слово с заглваной буквы"""
    return ' '.join(int_func(i) for i in x.split())
print(my_func1('how are you'))










