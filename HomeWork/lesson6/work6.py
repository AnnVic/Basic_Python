# Задание 1
import time
class TrafficLight:
    __color = None

    def running(self):
        print('red')
        time.sleep(7)
        print('yellow')
        time.sleep(2)
        print('green')
        time.sleep(6)


my_traffic = TrafficLight()
my_traffic.running()

# Задание 2
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

class Count(Road):
    def __init__(self, _length, _width, weight, thikness):
        super().__init__(_length, _width)
        self.weight = weight
        self.thikness = thikness

    def calculate_count(self):
        print (self._length * self._width * self.weight * self.thikness / 1000)

my_road2 = Count(20, 5000, 25, 5)
my_road2.calculate_count()

# Задание 3
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


a = Position('Alex', 'Vic', 2, 20000, 1000)
print(a.get_full_name())
print(a.get_total_income())

# Задание 4
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина поехала'

    def stop(self):
        return f'Машина остановилась'

    def turn(self, direction):
        return f'Машина повернула ' + direction

    def show_speed(self):
        return f'Скорость автомобиля {self.name} {self.speed} км/ч'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Вы превысили скорость!'
        else:
            return f'Вы соблюдаете скоростной режим'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Вы превысили скорость!'
        else:
            return f'Вы соблюдаете скоростной режим'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

a = Car(50, 'Red', 'Audi', False)
a1 = TownCar(64, 'Black', 'Toyota', False)
a2 = WorkCar(45, 'Blue', 'Audi', False)
a3 = PoliceCar(45, 'White', 'Dacia', True)
a4 = SportCar(120, 'Orange', 'Ferrari', False)
print(a1.color)
print(a.turn('направо'))
print(a3.is_police)
print(a1.show_speed())
print(a2.show_speed())

# Задание 5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Ручкой идет отрисовка {self.title}'

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Карандашом идет отрисовка {self.title}'


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Маркером идет отрисовка {self.title}'

a = Stationery('Sun')
a1 = Pen('Flower')
a2 = Pencil('Home')
a3 = Handle('Gift')
print(a.title)
print(a.draw())
print(a1.draw())
print(a2.draw())
print(a3.draw())












