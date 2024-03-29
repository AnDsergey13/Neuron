import Space
import Neuron
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
		on = True
		while on:
			# Генерируем новые координаты
			new_xyz = self.gen_xyz_neuron()
			# Новый нейрон НЕ должен появиться там, где есть уже другой нейрон
			for xyz in self.list_xyz:
				if new_xyz == tuple(xyz):
					#print("найдена копия координат, начинаем заново")
					break
			else:
				# если копии нет, то создаём нейрон со сгенерированными координатами
				# так же не создаём нейрон, если превышено максимальное значение по созданию
				if len(self.get_list_object()) + 1 < self.get_max_neurons():
					new_neuron = Neuron.Neuron(self.space, new_xyz[0], new_xyz[1], new_xyz[2])
					self.list_object.append(new_neuron)
					self.list_xyz.append([new_xyz[0], new_xyz[1], new_xyz[2]])
				# Выходим из цикла в любом случае, создали ли мы нейрон, или нет
				on = False	
		
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

	def start_loop(self, time_update=0.0001):
		create_th = threading.Thread(target=self.loop, args=(time_update,))
		create_th.start()

	def loop(self, time_update):
		while not self.shift.is_keyboard_pressed():

			######## ВРЕМЯ ОБНОВЛЕНИЯ ЦИКЛА
			# Без задержки виснет программа
			time.sleep(time_update)

			######## ЛОГИКА СОСТОЯНИЙ
			copy_list_obj_neuron = self.get_list_object().copy()
			for pos, obj_neuron in enumerate(copy_list_obj_neuron):
				status = obj_neuron.get_state()
				if status == 0:
					new_pos = obj_neuron.calc_new_pos()
					obj_neuron.set_pos(new_pos)
				if status == 5:
					# Пока не удаляем нейрон, а перемещаем в центр
					obj_neuron.set_pos((255, 255, 255))
					obj_neuron.set_state(0)

			# ######## ПОИСК БЛИЖАЙШИХ НЕЙРОНОВ
			# list_xyz_neurons = np.array(self.get_list_xyz())
			# list_object = self.get_list_object()
			# for obj in list_object:
			# 	# Получим координаты проверяемого нейрона
			# 	n_xyz = np.array(obj.get_pos())
			# 	# Получим радиус обнаружения проверяемого нейрона
			# 	n_radius_detection = obj.get_radius_searches()

			# 	detection_list = np.array([], dtype=bool)
			# 	for x, y, z in list_xyz_neurons:
			# 		# Считаем вектора для всех нейронов, относительно выбранного
			# 		x_, y_, z_ = np.array([x, y, z]) - n_xyz
			# 		# считаем расстояние от одного нейрона до другого
			# 		# а после, проверяем видит ли проверяемый нейрон, другого нейрона 
			# 		detect = (x_**2 + y_**2 + z_**2)**0.5 <= n_radius_detection
			# 		detection_list = np.append(detection_list, detect)
			# 	list_found_neurons = list_xyz_neurons[detection_list]
			# 	obj.update_nearest_neurons(np.array(list_found_neurons))



			######## ОБНОВЛЕНИЕ КООРДИНАТ
			copy_list_obj_neuron = self.get_list_object().copy()
			for pos, obj_neuron in enumerate(copy_list_obj_neuron):
				self.list_xyz[pos] = obj_neuron.get_pos()
			# print("координаты выполнены!")

			#### ОБНОВЛЕНИЕ СОСТОЯНИЯ
			# ВРЕМЕННАЯ РЕАЛИЗАЦИЯ ДЛЯ ТЕСТОВ
			# При выходе за пределы пространства, нейрон помечается состоянием = 5
			for obj_neuron in self.get_list_object():
				if not obj_neuron.is_space(mode="out"):
					obj_neuron.set_state(5)

			#### ПЕРДАЧА ДАННЫХ
			pass
		print("Loop close!!!")

	def get_max_neurons(self):
		return self.MAX_NEURONS

	def get_list_object(self):
		return self.list_object

	def get_list_xyz(self):
		return self.list_xyz
