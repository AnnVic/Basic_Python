# Задание 1
class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        day, month, year = day_month_year.split('-')
        my_date = day, month, year
        print(my_date[0], my_date[1], my_date[2])

    @staticmethod
    def validation(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 < year:
                    return f'Все правильно'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

my_data = Data('6-7-2020')
Data.extract('6-7-2020')
print(Data.validation(6, 7, 2020))

# Задание 2
class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

    inp_data = input('Ведите число ')
    try:
        inp_data = int(inp_data)
        res = inp_data / 0
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    finally:
        print('Конец')

# Задание 3
class MyError:
    def __init__(self, *args):
        self.my_list = []

    def list_input(self):
        while True:
            try:
                num = int(input('Введите число '))
                self.my_list.append(num)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f'Вы ввели не число')
                choice = input(f'Попробовать еще раз? Y/N ')

                if choice == 'Y' or choice == 'y':
                    print(self.my_list)
                elif choice == 'N' or choice == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'

my_error = MyError(1)
print(my_error.list_input())

# Задание 4, 5, 6
class Storage:
    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за ед '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'{self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'



class Printer(Storage):
    def to_print(self):
        return f'to print {self.numb} times'


class Scanner(Storage):
    def to_scan(self):
        return f'to scan {self.numb} times'


class Copier(Storage):
    def to_copier(self):
        return f'to copier {self.numb} times'

unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())


# Задание 7
class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'{self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        return f'{self.a * other.a} + {self.b * other.b}i'

number = ComplexNumber(2, 5)
number1 = ComplexNumber(2, 2)
print(number.__add__(number1))
print(number.__mul__(number1))











