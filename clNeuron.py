import numpy as np
import math

class Space:
    def __init__(self, number_points=8):
        """ number_points - количество точек (вершин) у пространства.
                По умолчанию геометрическая фигура куб (8 точек) """
        self.in_points = np.zeros((number_points, 3))
        self.out_points = np.zeros((number_points, 3))

    def set_points(self, points, th=10):
        """ Задаются точки для внешней области пространства. Генерируется точки для внутренней области.
                points - массив внешних(!) точек.
                    Пример записи для куба [[0, 0, 0], [0, 0, 99], [99, 0, 99], [99, 0, 0],[0, 99, 0], [0, 99, 99], [99, 99, 99], [99, 99, 0]]
                th - толщина внешней области пространства. По умолчанию 10 """
        self.out_points = points

        #####
        x, y, z = points[0] # Получаем координаты стартовой точки
        size_in_cube = self.size_out_cube - th * 2 # Вычисляем длину внутреннего пространства
        self.in_points = self.create_cube(x + th, y + th, z + th, size_in_cube + 1)

        #####

    def get_out_points(self):
        """ Возвращает массив точек (координат). Из внешней области пространства"""
        return self.out_points

    def get_in_points(self):
        """ Возвращает массив точек (координат). Из внутренней области пространства"""
        return self.in_points

    def create_cube(self, x=0, y=0, z=0, size=100):
        """ Создаёт и возвращает массив точек для куба.
                x,y,z(int) - начальная точка для создания куба
                size(int) - размер грани """
        #####
        self.size_out_cube = size - 1
        list_points = []

        def funcc():
            summ = 0
            offset = 0.8
            for point in range(8):
                summ = summ + offset
                yield math.sin(summ)

        def convert():
            koeff = next(a)
            return koeff < 0

        for plane in range(2):
            a = funcc()
            for point in range(4):
                koeff_x = convert()
                koeff_z = convert()
                list_points.append([x + koeff_x * self.size_out_cube, y, z + koeff_z * self.size_out_cube])
            y = y + self.size_out_cube

        return np.array(list_points)
        #####


class Neuron():
    def __init__(self, x, y, z):
        #self.list_input = []
        #self.list_output = []
        self.x_pos = x
        self.y_pos = y
        self.z_pos = z

    def set_pos(self):
        offset = 20
        self.x_pos = self.x_pos + offset
        self.y_pos = self.y_pos + offset
        self.z_pos = self.z_pos + offset

    def get_pos(self):
        return self.x_pos, self.y_pos, self.z_pos

    def is_internal_space(self):
        """ Возвращает True, если нейрон находится во внутренней зоне пространства.
            А False, когда во внешней зоне."""

        in_space = space.get_in_points()
        if (self.z_pos > in_space[0][2] and self.z_pos < in_space[1][2]) and (self.y_pos > in_space[0][1] and self.y_pos < in_space[4][1]) and (self.x_pos > in_space[0][0] and self.x_pos < in_space[2][0]):
            return True
        else:
            return False




space = Space()
out_p = space.create_cube(size=50)
space.set_points(out_p, 10)
print(space.get_out_points())
print(space.get_in_points())
a = Neuron(13, 20, 23)
print(a.get_pos())
print(a.is_internal_space())
a.set_pos()
print(a.get_pos())
print(a.is_internal_space())











