import pygame
import threading

class Drawing():
	""" Класс для работы с графикой	"""

	def __init__(self, name="Hello, pygame!", screen_width=1000, screen_height=500, 
		bot_width=5, bot_height=5, text_height=25):
		""" Начальные условия
			Создание окна, инициализация объекта класса pygame, 
			название окна, стиль текста, размер пикселей/ботов и т.д. 
		"""
		pygame.init()
		self.screen_width = screen_width
		self.screen_height = screen_height
		self.window = pygame.display.set_mode((self.screen_width, self.screen_height))
		self.fontObj = pygame.font.SysFont('verdana', text_height)
		# ?
		self.bot = pygame.Surface((bot_width, bot_height))
		# ?
		pygame.display.set_caption(name)

	def clear_pos_bot(self, bot):
		""" Очищаем место где был бот раньше на экране """
		# меняем цвет бота
		bot.fill((0, 0, 0))

	def draw_object(self, window, object_, x, y):
		""" Преносим изменения на экран """
		# обновляем переменные 
		self.object_ = object_
		self.x = x
		self.y = y
		window.blit(object_, (x, y))

	def clear_text(self, object_):
		""" Закрашиваем чёрным место, где отрисовывается текст"""
		object_ = self.fontObj.render("█████", 1, (0, 0, 0), (0, 0, 0))
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

	def get_pos_mouse(self):
		""" Возвращает кортеж x и y позиции мышки"""
		return pygame.mouse.get_pos()

	def check_object_on_screen(self, x, y):
		""" Возвращает True, если объект находится в зоне окна, иначе False """
		if x > 0 and x < screen_width and y > 0 and y < screen_height:
			return True
		else:
			return False