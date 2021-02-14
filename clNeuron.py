import numpy as np

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
        points_in = points.copy()
        points_in = np.where(points_in == points_in.min(), points_in + th, points_in)
        points_in = np.where(points_in == points_in.max(), points_in - th, points_in)
        self.in_points = points_in

    def get_out_points(self):
        """ Возвращает массив точек (координат). Из внешней области пространства"""
        return self.out_points

    def get_in_points(self):
        """ Возвращает массив точек (координат). Из внутренней области пространства"""
        return self.in_points

    def create_cube(self, size=100):
        """ Создаёт и возвращает массив точек для куба.
                size(int) - размер грани """
        return np.array([[0, 0, 0], [0, 0, size - 1], [size - 1, 0, size - 1], [size - 1, 0, 0],[0, size - 1, 0], [0, size - 1, size - 1], [size - 1, size - 1, size - 1], [size - 1, size - 1, 0]])

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




# space = Space()
# out_p = space.create_cube(50)
# space.set_points(out_p, 15)
# print(space.get_out_points())
# print(space.get_in_points())
# a = Neuron(3, 10, 13)
# print(a.get_pos())
# print(a.is_internal_space())
# a.set_pos()
# print(a.get_pos())
# print(a.is_internal_space())










