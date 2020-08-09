import pygame
import threading

class Drawing():
	""" Класс для работы с графикой	"""

	def __init__(self):
		"""  Создание окна, инициализация объекта класса pygame, 
		название окна, стиль текста, размер пикселей/ботов  """
		pass

	def update_varible(self, *varible):
		# как обновить сразу все переменные?
		self.bot = bot
		self.window = window
		self.x = x
		self.y = y

	def clear_pos_bot(self, bot):
		""" Очищаем место где был бот раньше на экране """
		# меняем цвет бота
		bot.fill((0, 0, 0))

	def draw_object(self, window, object_, x, y):
		""" Преносим изменения на экран """
		self.update_varible(window, object_, x, y)
		window.blit(object_, (x, y))

	def clear_text(self, object_):
		""" Закрашиваем чёрным место, где отрисовывается текст"""
		object_ = fontObj.render("█████", 1, (0, 0, 0), (0, 0, 0))
		# text1 = fontObj.render(
		# "\u2588\u2588\u2588\u2588\u2588", 1, (0, 0, 0), (0, 0, 0))  # alt + 219

	def draw_num_th(self, object_):
		""" Рисуем количество активных потоков """
		num_TH = str(threading.active_count())
		object_ = fontObj.render(num_TH, 1, (0, 255, 0))

	def update_screen(self):
		""" Обновляем картинку для всех объектов на экране"""
		pygame.display.flip()
		pygame.time.delay(self.delay_update)

	def set_delay(self, delay_update):
		""" Установить задержку для каждой отрисовки"""
		self.delay_update = delay_update