import pygame

class Event_mouse_and_keyboard():
	""" DOC	"""
	block = False

	def __init__():
		"""  Стартовые параметры """
		pass

	def keyboard_pressed(self, key_p, function):
		"""
		key_p - нажимаемая клавиша. клавиатура(pygame.K_SPACE)  # Стиль имени!
		function - запускаемая функция после события
		Example. key_pressed(pygame.K_SPACE, pause_ses)  # Стиль имени!
		"""

		if pygame.key.get_pressed()[key_p] == 1:

			if not Event_mouse_and_keyboard.block:
				# print(block_keyboard)
				time.sleep(0.5)
				Event_mouse_and_keyboard.block = True
				function()
		else:
			Event_mouse_and_keyboard.block = False


	def mouse_pressed(self, key_p, function):
		"""
		key_p - нажимаемая клавиша ЛКМ(0),СКМ(1),ПКМ(2)
		function - запускаемая функция после события
		Example. key_pressed(0, closed)
		"""

		if pygame.mouse.get_pressed()[key_p] == 1:  # мышь
			if not Event_mouse_and_keyboard.block:
				# print(block_mouse)
				Event_mouse_and_keyboard.block = True
				function()
		else:
			Event_mouse_and_keyboard.block = False