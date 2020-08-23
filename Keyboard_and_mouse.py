import pygame

	""" DOC	"""
	def __init__(self):
class Event():
		"""  Стартовые параметры """
		self.block = False

	def keyboard_pressed(self, key_p, function):
		"""
		key_p - нажимаемая клавиша. клавиатура(pygame.K_SPACE)  # Стиль имени!
		function - запускаемая функция после события
		Example. key_pressed(pygame.K_SPACE, pause_ses)  # Стиль имени!
		"""

		if pygame.key.get_pressed()[key_p] == 1:

			if not self.block:
				# print(block_keyboard)
				# time.sleep(0.5)
				self.block = True
				function()
		else:
			self.block = False

	def is_keyboard_pressed(self, key_p):
		"""
		key_p - нажимаемая клавиша. клавиатура(pygame.K_SPACE)
		Example. is_keyboard_pressed(pygame.K_SPACE)
		"""

		if pygame.key.get_pressed()[key_p] == 1:

			if not self.block:
				# print(block_keyboard)
				# time.sleep(0.5)
				self.block = True
				return True
		else:
			self.block = False
			return False


	def mouse_pressed(self, key_p, function):
		"""
		key_p - нажимаемая клавиша ЛКМ(0),СКМ(1),ПКМ(2)
		function - запускаемая функция после события
		Example. mouse_pressed(0, closed)
		"""

		if pygame.mouse.get_pressed()[key_p] == 1:  # мышь
			if not self.block:
				# print(block_mouse)
				self.block = True
				function()
		else:
			self.block = False


	def is_mouse_pressed(self, key_p):
		"""
		key_p - нажимаемая клавиша ЛКМ(0),СКМ(1),ПКМ(2)
		Example. is_mouse_pressed(0)
		"""

		if pygame.mouse.get_pressed()[key_p] == 1:  # мышь
			if not self.block:
				# print(block_mouse)
				self.block = True
				return True
		else:
			self.block = False
			return False


