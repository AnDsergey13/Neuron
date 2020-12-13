# -*- coding: utf-8 -

import keyboard
import mouse


class Event():
	""" Класс для работы с клавиатурой и мышью """

	def __init__(self, key_p):
		"""  Стартовые параметры """
		self.block = False
		try:
			self.key_p = key_p
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

		if keyboard.is_pressed(self.key_p):

			if not self.block:
				self.block = True
				function()
		else:
			self.block = False

	def is_keyboard_pressed(self):
		"""
		Возвращает True если была нажата клавиша на клавиатуре.
		"""

		if keyboard.is_pressed(self.key_p):

			if not self.block:
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

		if mouse.is_pressed(button=self.key_p):  # мышь
			if not self.block:
				self.block = True
				function()
		else:
			self.block = False

	def is_mouse_pressed(self):
		"""
		Возвращает True если была нажата клавиша на мыши.
		"""

		if mouse.is_pressed(button=self.key_p):  # мышь
			if not self.block:
				self.block = True
				return True
		else:
			self.block = False
			return False
	# del ?
	# def get_list_key(self):
	# 	""" Возвращает список зарезервированных клавиш """
	# 	return list(Event.key_object.keys())
