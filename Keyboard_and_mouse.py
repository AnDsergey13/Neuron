import pygame

class Event():
	""" Класс для работы с клавиатурой и мышью """
	key_object = {
		# Левая кнопка мыши
		"lbm" : 0,
		# Средняя кнопка мыши
		"mbm" : 1,
		# Средняя кнопка мыши
		"rbm" : 2,
		"space" : pygame.K_SPACE,
		"0" : pygame.K_0,
		"1" : pygame.K_1,
		"2" : pygame.K_2,
		"3" : pygame.K_3,
		"4" : pygame.K_4,
		"5" : pygame.K_5,
		"6" : pygame.K_6,
		"7" : pygame.K_7,
		"8" : pygame.K_8,
		"9" : pygame.K_9,
		"a" : pygame.K_a,
		"b" : pygame.K_b,
		"c" : pygame.K_c,
		"d" : pygame.K_d,
		"e" : pygame.K_e,
		"f" : pygame.K_f,
		"g" : pygame.K_g,
		"h" : pygame.K_h,
		"i" : pygame.K_i,
		"j" : pygame.K_j,
		"k" : pygame.K_k,
		"l" : pygame.K_l,
		"m" : pygame.K_m,
		"n" : pygame.K_n,
		"o" : pygame.K_o,
		"p" : pygame.K_p,
		"q" : pygame.K_q,
		"r" : pygame.K_r,
		"s" : pygame.K_s,
		"t" : pygame.K_t,
		"u" : pygame.K_u,
		"v" : pygame.K_v,
		"w" : pygame.K_w,
		"x" : pygame.K_x,
		"y" : pygame.K_y,
		"z" : pygame.K_z
	}
	def __init__(self, key_p):
		"""  Стартовые параметры """
		self.block = False
		try:
			self.key_p = Event.key_object.get(key_p)
		except:
			print(""" 
				Ошибка ввода! Нет такой клавиши.
				Используйте метод get_list_key(), чтобы посомтреть зарезервированные имена клавиш.
				""")
		

	def keyboard_pressed(self, function):
		"""
		function - запускаемая функция после события
		Example. key_pressed(function)
		"""

		if pygame.key.get_pressed()[self.key_p] == 1:

			if not self.block:
				# print(block_keyboard)
				# time.sleep(0.5)
				self.block = True
				function()
		else:
			self.block = False

	def is_keyboard_pressed(self):
		"""
		Возвращает True если была нажата клавиша на клавиатуре. 
		"""

		if pygame.key.get_pressed()[self.key_p] == 1:

			if not self.block:
				# print(block_keyboard)
				# time.sleep(0.5)
				self.block = True
				return True
		else:
			self.block = False
			return False


	def mouse_pressed(self, function):
		"""
		function - запускаемая функция после события
		Example. mouse_pressed(function)
		"""

		if pygame.mouse.get_pressed()[self.key_p] == 1:  # мышь
			if not self.block:
				# print(block_mouse)
				self.block = True
				function()
		else:
			self.block = False


	def is_mouse_pressed(self):
		"""
		Возвращает True если была нажата клавиша на мыши. 
		"""

		if pygame.mouse.get_pressed()[self.key_p] == 1:  # мышь
			if not self.block:
				# print(block_mouse)
				self.block = True
				return True
		else:
			self.block = False
			return False


