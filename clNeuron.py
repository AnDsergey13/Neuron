import numpy as np

class Neuron:
    # Координаты вершин куба
    # Пример структуры [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    space_in = np.zeros((8, 3))
    space_out = np.zeros((8, 3))

    def __init__(self, xyz_pos):
        #self.list_input = []
        #self.list_output = []
        self.x_pos = xyz_pos[0]
        self.y_pos = xyz_pos[1]
        self.z_pos = xyz_pos[2]

    @staticmethod
    def set_point_space(points, th=10):
        """ 1 аргумент - точки геометрической фигуры (пространства).
            2 аргумент - толщина внешней области. По умолчанию 10"""
        Neuron.space_out = points
        points_in = points.copy()
        points_in = np.where(points_in == points_in.min(), points_in + th, points_in)
        points_in = np.where(points_in == points_in.max(), points_in - th, points_in)
        Neuron.space_in = points_in

    @staticmethod
    def get_point_out_space():
        return Neuron.space_out

    @staticmethod
    def get_point_in_space():
        return Neuron.space_in

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

        in_space = self.get_point_in_space()
        if (self.z_pos > in_space[0][2] and self.z_pos < in_space[1][2]) and (self.y_pos > in_space[0][1] and self.y_pos < in_space[4][1]) and (self.x_pos > in_space[0][0] and self.x_pos < in_space[2][0]):
            return True
        else:
            return False







#print(Neuron.get_point_out_space())
#print(Neuron.get_point_in_space())
#Neuron.set_point_space(np.array([[0, 0, 0], [0, 0, 99], [99, 0, 99], [99, 0, 0],[0, 99, 0], [0, 99, 99], [99, 99, 99], [99, 99, 0]]))
#print(Neuron.get_point_out_space())
#print(Neuron.get_point_in_space())





