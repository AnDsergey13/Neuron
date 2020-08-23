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
	def loop(self):
		""" Цикл в котором всё происходит """
	def movement(self):
		""" В этом методе описано движение бота """
