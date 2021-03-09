# -*- coding: utf-8 -
#from Keyboard_and_mouse import Event
from clNeuron import Space, Neuron
import Neuron_controller as nc
import Interface as ui
#import keyboard
import numpy as np

def full_completion_space():
	while control.is_max_neurons():
		control.create_neuron()
		print(len(control.get_list_xyz()))
	print("Заполнение завершено успешно!")


MAX_NEURONS = 100

space = Space()
out_p = space.create_cube(10, 10, 0, size=50)
space.set_points(out_p, 1)

# print(space.get_out_points())
# print(space.get_in_points())

control = nc.Controller(space)
#full_completion_space()

# Interface
# # =================================
# a = Window(1000, 800, 0, 0)
# # a.set_color_grid(255, 255, 255, 10)
# # a.create_grid()
# a.set_coord()
# a.create_line(np.array([[10,10,10],[10,10,29],[29,10,29],[29,10,10],[10,29,10],[10,29,29],[29,29,29],[29,29,10]]))
# a.print_window()

# =================================

# print(a.get_pos())
# print(a.is_internal_space())
# a.move(15, 25, 40)
# print(a.get_pos())
# print(a.is_internal_space())

# print("------------------")
# print(gen_coord_neuron())
# =================================
# size_x = 10
# size_y = 10

# c = Event("c")

# # создаём поле
# pole = np.ones((size_x, size_y), int)
# # Заполняем поле нулями
# pole.fill(0)

# while not keyboard.is_pressed("space"):
# 	pass
# 	if c.is_keyboard_pressed():
# 		print(str(pole))
