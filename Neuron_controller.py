from clNeuron import Space,Neuron
from Keyboard_and_mouse import Event
import numpy as np
import random
import threading
import time

class Controller:
	def __init__(self, obj_space, max_neuron=None):
		self.space = obj_space
		if max_neuron == None:
			number = self.calc_max_neuron_cube(self.space.get_out_points())
			self.set_max_neurons(number)
		else:
			self.set_max_neurons(max_neuron)

		self.list_object = []
		self.list_xyz = []

		self.shift = Event("esc")
		

	def calc_max_neuron_cube(self, out_points):
		""" Возвращает максимальное число нейронов, которое может пометиться в заданном пространстве """
		x_delta = abs(out_points[0][0] - out_points[2][0]) - 1
		y_delta = abs(out_points[0][1] - out_points[4][1]) - 1
		z_delta = abs(out_points[0][2] - out_points[1][2]) - 1
		return x_delta * y_delta * z_delta

	def create_neuron(self):
		""" Создаёт нейрон в случайном месте пространства """
		new_xyz = self.gen_xyz_neuron()
		for xyz in self.list_xyz:
			if new_xyz == tuple(xyz):
				#print("найдена копия, начинаем заново")
				break
		else:
			#print("копии нет, создаём нейрон")
			# self.list_object.append(Neuron(self.space, new_xyz[0], new_xyz[1], new_xyz[2]))
			self.list_object.append(Neuron(self.space))
			self.list_xyz.append([new_xyz[0], new_xyz[1], new_xyz[2]])
		# else:
		# 	print("Привышено максимальное количество нейронов для данной области")	

	def is_max_neurons(self):
		""" Возвращает True, если можно создать нейрон в области """
		return len(self.list_object) < self.get_max_neurons()

	def gen_xyz_neuron(self):
		""" Возвращает кортеж с новыми координатами нейрона """
		out_points = self.space.get_out_points()
		x = random.randrange(out_points[0][0] + 1, out_points[2][0])
		y = random.randrange(out_points[0][1] + 1, out_points[4][1])
		z = random.randrange(out_points[0][2] + 1, out_points[1][2])
		return x, y, z

	def set_max_neurons(self, number):
		""" Задать вручную максимальное количество нейронов в пространстве"""
		self.MAX_NEURONS = number

	def start_loop(self):
		create_th = threading.Thread(target=self.loop)
		create_th.start()

	def loop(self):
		while not self.shift.is_keyboard_pressed():
			time.sleep(0.03)
			# Движение
			for obj_neuron in self.get_list_object():
				status = obj_neuron.get_state()
				if status == 0:
					obj_neuron.move()
					# if obj_neuron.is_internal_space():
						
					# else:
					# 	print("output zone!!!")
			# print("движение выполнено!")
			# Обновление координат
			copy_list_obj_neuron = self.get_list_object().copy()
			for pos, obj_neuron in enumerate(copy_list_obj_neuron):
				self.list_xyz[pos] = obj_neuron.get_pos()
			# print("координаты выполнены!")
			# Предача данных
			pass
		print("Loop close!!!")

	def get_max_neurons(self):
		return self.MAX_NEURONS

	# ?
	def get_list_object(self):
		return self.list_object

	def get_list_xyz(self):
		return self.list_xyz


# def next(number_changes):
#     list_random_changes = [random.randrange(0, NUM_NEURONS) for i in range(number_changes)]
#     for num in list_random_changes:
#         list_object[num].next_step()

# def next_all():
#     for num in range(NUM_NEURONS):
#         list_object[num].next_step()

# def see_all_changes():
#     for num in range(len(list_object)):
#         print(f"{num}..{list_object[num].get_pos()}")

