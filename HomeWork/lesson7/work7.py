# Задание 1
class Matrix:
    def __init__(self, my_list, my_list1):
        self.my_list = my_list
        self.my_list1 = my_list1

    def __add__(self):
        matrix = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.my_list)):
            for j in range(len(self.my_list1[i])):
                matrix[i][j] = self.my_list[i][j] + self.my_list1[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix]))

a = Matrix([[5, 18, 11],
            [6, 17, 23],
            [41, 50, 9]],
            [[45, 8, 2],
            [6, 7, 93],
            [24, 5, 97]])
print(a.__add__())


# Задание 2
from abc import ABC
class Clothing(ABC):
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def calculate_textile(self):
        return self.size / 6.5 + 0.5

    def calculate_textile2(self):
        return self.height * 2 + 0.3

    @property
    def total_textile(self):
        return str(f'{(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}')

class Coat(Clothing):
    def calculate_textile(self):
        return self.size / 6.5 + 0.5


class Costume(Clothing):
    def calculate_textile2(self):
        return self.height * 2 + 0.3


clothing = Clothing(36, 160)
print(clothing.total_textile)
coat = Coat(48, 170)
print(coat.calculate_textile())
costume = Costume(50, 100)
print(costume.calculate_textile2())

# Задание 3
class Cell:
    def __init__(self, number, row=None):
        self.number = number
        self.row = row


    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number - other.number > 0:
            return Cell(self.number - other.number)
        else:
            return f'Операция невозможна'

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(self.number // other.number)


cell2 = Cell(250, 5)
cells = Cell(5, 2)
a = cell2 / cells
print(a.number)

























