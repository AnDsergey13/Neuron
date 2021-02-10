import numpy as np

class Neuron:
    # Координаты вершин тэтрадра
    # Пример структуры [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    space = np.zeros((4, 3))

    def __init__(self, xyz_pos):
        self.list_input = []
        self.list_output = []
        self.x_pos = xyz_pos[0]
        self.y_pos = xyz_pos[1]
        self.z_pos = xyz_pos[2]

    @staticmethod
    def set_point_space(points):
        Neuron.space = points

    @staticmethod
    def get_point_space():
        return Neuron.space

    def set_pos(self):
        offset = 2
        self.x_pos = self.x_pos + offset
        self.y_pos = self.y_pos + offset
        self.z_pos = self.z_pos + offset

    def get_pos(self):
        return self.x_pos, self.y_pos, self.z_pos





#print(Neuron.get_point_space())
Neuron.set_point_space(np.array([[157, 171, 0], [0, -16, 0], [230, -50, 75], [75, 81, 212]]))
#print(Neuron.get_point_space())
a = Neuron([5, 10, -7])













