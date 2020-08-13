import pygame

class Drawing():
	""" Класс для работы с графикой	"""
	color_object = {
		"red" : (255, 0, 0),
		"orange" : (255, 128, 0),
		"yellow" : (255, 255, 0),
		"green" : (0, 255, 0),
		"light blue" : (0, 255, 255),
		"dark blue" : (0, 0, 255),
		"purple" : (255, 0, 255),
		"black" : (0, 0, 0),
		"white" : (255, 255, 255)
	}

	def __init__(self, name="Hello, pygame!", screen_width=700, screen_height=500, text_height=25):
		""" Начальные условия
			Создание окна, инициализация объекта класса pygame, 
			название окна, стиль текста, и т.д. 
		"""
		pygame.init()
		self.screen_width = screen_width
		self.screen_height = screen_height
		self.window = pygame.display.set_mode((self.screen_width, self.screen_height))
		self.fontObj = pygame.font.SysFont("verdana", text_height)

		pygame.display.set_caption(name)

	def clear_pos_bot(self):
		""" Очищаем место где был бот раньше на экране """
		# меняем цвет бота
		self.bot.fill(Drawing.color_object.get("black"))

	def create_bot(self, bot_width=5, bot_height=5):
		""" Создаём объект бота """
		self.bot = pygame.Surface((bot_width, bot_height))

	def draw_bot(self, x, y):
		""" Преносим изменения на экран """
		self.window.blit(self.bot, (x, y))

	def set_color_bot(self, *color):
		""" Задаём цвет для бота.
			Допускается надписи типа "red", а также в RGB виде """
		if len(color) == 3:
			self.bot.fill(color)
		elif len(color) == 1:
			# достаём строку из кортежа
			color = color[0]
			# если пришёл только один аргумент, то это строка
			self.bot.fill(Drawing.color_object.get(color))
		else:
			print("""
				Ошибка ввода! Введите название цвета или его RGB формат.
				ПРИМЕРЫ! set_color_bot("light blue") или set_color_bot(0, 255, 255)
				Для уточнения, какие цвета можно использовать, введите get_list_colors()
			""")

	def clear_text(self):
		""" Закрашиваем чёрным место, где отрисовывается текст"""
		self.text = self.fontObj.render("█████", 1, Drawing.color_object.get("black"),
										Drawing.color_object.get("black"))

	# text1 = fontObj.render(
	# "\u2588\u2588\u2588\u2588\u2588", 1, (0, 0, 0), (0, 0, 0))  # alt + 219

	def draw_text(self, *color, value):
		""" Задаём цвет для текста.
			Допускается надписи типа "red", а также в RGB виде
			ПРИМЕР! py.draw_text("purple", value=num_th)
		"""
		if len(color) == 3:
			self.text = self.fontObj.render(str(value), 1, color)
		elif len(color) == 1:
			color = color[0]
			self.text = self.fontObj.render(str(value), 1, Drawing.color_object.get(color))
		else:
			print("""
				Ошибка ввода! Введите название цвета или его RGB формат.
				ПРИМЕРЫ! draw_num_th("light blue") или draw_num_th(0, 255, 255)
				Для уточнения, какие цвета можно использовать, введите get_list_colors()
			""")
		
	def update_screen(self):
		""" Обновляем экран без задержки"""
		pygame.display.flip()

	def update_screen_with_delay(self, delay_update=0):
		""" Обновляем экран c задержкой. По умолчанию задержка 0"""
		pygame.display.flip()
		pygame.time.delay(delay_update)

	# del?
	def set_delay(self, delay_update):
		""" Установить задержку для каждой отрисовки"""
		self.delay_update = delay_update

	def get_pos_mouse(self):
		""" Возвращает кортеж x и y позиции мышки"""
		return pygame.mouse.get_pos()

	def check_object_on_screen(self, pos):
		""" Возвращает True, если объект находится в зоне окна, иначе False """
		# на вход принимается кортеж
		# pos[0] - это x, pos[1] - это y
		if pos[0] > 0 and pos[0] < self.screen_width and pos[1] > 0 and pos[1] < self.screen_height:
			return True
		else:
			return False

	def get_list_colors(self):
		return list(Drawing.color_object.keys())