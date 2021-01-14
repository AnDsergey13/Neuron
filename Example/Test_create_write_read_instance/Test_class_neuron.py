import random

class Neuron:
    def __init__(self, name="test"):
        self.name = name
        self.x_pos = 0
        self.y_pos = 0
        self.z_pos = 0

    def next_step(self):
        """
        x_offset = random.randrange(-15, 15)
        y_offset = random.randrange(-15, 15)
        z_offset = random.randrange(-15, 15)
        """
        offset = 2
        self.x_pos = self.x_pos + offset
        self.y_pos = self.y_pos + offset
        self.z_pos = self.z_pos + offset

    def get_pos(self):
        return self.x_pos, self.y_pos, self.z_pos