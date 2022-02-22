import Space
import Neuron
import Neuron_controller as nc
import Interface as ui
#import keyboard
import numpy as np
import time


MAX_NEURONS = 25
SIZE_CUBE = 500

space = Space.Space()
out_p = space.create_cube(10, 10, 0, size=SIZE_CUBE)
space.set_points(out_p, 30)

control = nc.Controller(space, MAX_NEURONS)
control.start_loop()

for i in range(MAX_NEURONS):
	control.create_neuron()

# Interface
# # =================================

window = ui.Window(1000, 800, 400, 100, 200)
window.draw_neurons(control, size_point=5, time_update=5)

window.set_color_grid(255, 255, 255, 35)
window.draw_grid(size=SIZE_CUBE)

window.draw_axis_xyz(size=SIZE_CUBE)

line_out_cube = window.gen_line_for_cube(space.get_out_points())
line_in_cube = window.gen_line_for_cube(space.get_in_points())
window.draw_line(line_out_cube, "yellow")
window.draw_line(line_in_cube, "purple")

window.print_window()


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

# ===========================
# def full_completion_space():
# 	while control.is_max_neurons():
# 		control.create_neuron()

# 		list_xyz = control.get_list_xyz()
# 		xyz = np.array(list_xyz[-1])
# 		window.create_point(xyz, 1)
# 		time.sleep(0.1)

# 		window.update()
# 		# print(len(control.get_list_xyz()))
# 	print("Заполнение завершено успешно!")
# ====================================
# for i in range(1000):
# 	control.create_neuron()
# 	list_xyz = control.get_list_xyz()
# 	xyz = np.array(list_xyz[i])
# 	print(type(xyz), xyz)
# 	window.create_point(xyz)
# full_completion_space()