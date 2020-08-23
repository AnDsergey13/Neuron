from Drawing import *

import pygame
import math
import threading
import numpy as np

class Neuron_(Drawing):
	""" Класс для работы с ботами """

	def __init__(self, mode=1):
		""" mode = 0 - без потоков 
			mode = 1 - это когда один бот в одном потоке 
		"""
		if mode == 1:
			create_th = threading.Thread(target=self.create_bot)
			create_th.start()

	def create_bot(self):
		""" Промежуточный метод в котором создаётся бот """
		self.x_bot, self.y_bot = self.get_pos_mouse()
		self.neuron = Bot()
		self.loop()	

	def loop(self):
		""" Цикл в котором всё происходит """
		while on:
			if pause_session:
				continue
			self.neuron.clear_pos_bot()
			self.neuron.draw_bot(self.x_bot, self.y_bot)

			# Метод для описания поведения движения
			self.movement()

			# если выход за пределы комнаты, то удаление
			if not self.check_object_on_screen((self.x_bot, self.y_bot)):
				self.neuron.clear_pos_bot()
				break

			# Меняем случайно цвет бота 
			self.neuron.set_color_bot(np.random.randint(140, 255), np.random.randint(140, 255), 255)
			
			self.neuron.draw_bot(self.x_bot, self.y_bot)
			self.update_screen()

	def movement(self):
		""" В этом методе описано движение бота """
		self.x_bot += math.sin(self.x_bot) * 5
		self.y_bot += -math.cos(self.y_bot) * 5
