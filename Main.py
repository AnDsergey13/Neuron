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

#full_completion_space()
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
