# Задание 1
name = 'Anna'
age = 20
print(name)
print(age)
surname = input('Какая у вас фамилия? ')
print('Ваша фамилия ' + surname)
user_age = input('Сколько вам лет? ')
print('Вам ' + user_age + ' лет')

# Задание 2
seconds = int(input('Введите количество секунд '))
hour = seconds // 3600
minutes = seconds % 3600 // 60
second = seconds % 3600 % 60
print(f'{hour}:{minutes}:{second}')

# Задание 3
num = input('Введите число ')
sum = int(num) + int((num + num)) + int((num + num + num))
print(sum)

# Задание 4
number = int(input('Пожалуйста введите целое число '))
maxnum = 0
while number > 0:
    if number % 10 > maxnum:
        maxnum = number % 10
    number = number // 10
print(maxnum)

# Задание 5
profit = int(input('Введите количество вырученных средств '))
waste = int(input('Введите сумму издержек '))
if profit > waste:
    print('Поздравляем с прибылью!')
    money_profit = profit - waste
    gain = money_profit / profit * 100
    print(f'Рентабельность составляет {gain.__round__(2)}%')
    worker = input('Введите число работников фирмы ')
    worker_profit = money_profit / int(worker)
    print(f'Прибыль на одного сотрудника составляет {worker_profit}')
elif profit < waste:
    print('К сожалению у вас убыток.')

# Задание 6
a = int(input('Сколько км вы пробежали в первый день? '))
b = int(input('Сколько км в результате, вы хотели бы достичь? '))
d = 1
while b >= a:
    print(f'В {d} день вы пробежали {a.__round__(2)} км')
    a = a + (a / 100 * 10)
    d += 1
print(f'На {d} день вы достигните желаемого результата, пробежав не менее {b} км')
