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

	pygame.init()
	screen_width = 700
	screen_height = 500
	window = pygame.display.set_mode((screen_width, screen_height))

	def __init__(self):
		""" DOC """
		pass

	def set_name_window(self, name="Hello, pygame!"):
		""" Устанавливаем имя окна.
			ПРИМЕР! py.set_name_window("Rembo") """
		self.name = name
		pygame.display.set_caption(name)

	def set_size_window(self, width=screen_width, height=screen_height):
		""" Установка размера экрана 
			ПРИМЕР! py.set_size_window(width, height) или py.set_size_window(500, 700)"""
		Drawing.screen_width = screen_width
		Drawing.screen_height = screen_height
		Drawing.window = pygame.display.set_mode((Drawing.screen_width, Drawing.screen_height))
		
	def update_screen(self):
		""" Обновляем экран без задержки"""
		pygame.display.flip()

	def update_screen_with_delay(self, delay_update=0):
		""" Обновляем экран c задержкой. По умолчанию задержка 0 милисекунд.
			ПРИМЕР! py.update_screen_with_delay(10)"""
		pygame.display.flip()
		pygame.time.delay(delay_update)

	# del?
	def set_delay(self, delay_update):
		""" Установить задержку для каждой отрисовки. Значения в милисекундах.
			ПРИМЕР! py.set_delay(10)"""
		self.delay_update = delay_update

	def get_pos_mouse(self):
		""" Возвращает кортеж x и y позиции мышки"""
		return pygame.mouse.get_pos()

	def check_object_on_screen(self, pos):
		""" Возвращает True, если объект находится в зоне окна, иначе False """
		# на вход принимается кортеж
		# pos[0] - это x, pos[1] - это y
		if pos[0] > 0 and pos[0] < Drawing.screen_width and pos[1] > 0 and pos[1] < Drawing.screen_height:
			return True
		else:
			return False

	def get_list_colors(self):
		return list(Drawing.color_object.keys())


class Bot(Drawing):
	""" Подкласс для работы с отрисовкой ботов """

	def __init__(self, bot_width=3, bot_height=3):
		""" Создаём объект бота """
		self.bot = pygame.Surface((bot_width, bot_height))

	def clear_pos_bot(self):
		""" Очищаем место где был бот раньше на экране """
		# меняем цвет бота на чёрный
		self.bot.fill(Drawing.color_object.get("black"))

	def draw_bot(self, x, y):
		""" Преносим изменения на экран """
		Drawing.window.blit(self.bot, (x, y))

	def set_color_bot(self, *color):
		""" Задаём цвет для бота.
			Допускается надписи типа "red", а также в RGB виде 
			ПРИМЕР! test.set_color_bot("light blue") или test.set_color_bot(0, 255, 255)
			Для уточнения, какие цвета можно использовать, введите py.get_list_colors()
		"""
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
				ПРИМЕРЫ! test.set_color_bot("light blue") или test.set_color_bot(0, 255, 255)
				Для уточнения, какие цвета можно использовать, введите py.get_list_colors()
			""")


class Text(Drawing):
	""" Подкласс для работы с отрисовкой текста """

	def __init__(self, x=15, y=15, h=25, style="verdana"):
		""" Инициализируем стартовые параметры.
			Такие как координаты x и y. Высота текста и его стиль 
			ПРИМЕР! test = Text(x, y, h, style) или test = Text(16, 71, 10, "verdana")
		"""
		pygame.font.init()
		self.x_text = x
		self.y_text = y
		self.fontObj = pygame.font.SysFont(style, h)
		# по умолчанию ставим белый текст 
		self.set_color_text("white")

	def clear_text(self):
		""" Закрашиваем чёрным место, где отрисовывается текст"""
		self.text = self.fontObj.render("██████████", 1, Drawing.color_object.get("black"),
										Drawing.color_object.get("black"))
		Drawing.window.blit(self.text, (self.x_text, self.y_text))
		# text1 = fontObj.render(
		# "\u2588\u2588\u2588\u2588\u2588", 1, (0, 0, 0), (0, 0, 0))  # alt + 219

	def set_color_text(self, *color):
		""" Задаём цвет для текста.
			В установке цвета допускается надписи типа "red", а также в RGB виде
			ПРИМЕР! test.draw_text("purple") или test.draw_text(255, 0, 255) # фиолетовый
		"""
		self.color_text = color

	def pos_text(self, x=15, y=15):
		""" Задаём позицию для текста. 
			ПРИМЕР!test.pos_text(x, y) 
		"""
		self.x_text = x
		self.y_text = y

	def draw_text(self, value):
		""" Рисуем заданный текст по координатам.
			ПРИМЕР! test.draw_text(5467)
			Нарисовано число 5467
		"""
		if len(self.color_text) == 3:
			self.text = self.fontObj.render(str(value), 1, self.color_text)
			Drawing.window.blit(self.text, (self.x_text, self.y_text))
		elif len(self.color_text) == 1:
			color_text = self.color_text[0]
			self.text = self.fontObj.render(str(value), 1, Drawing.color_object.get(color_text))
			Drawing.window.blit(self.text, (self.x_text, self.y_text))
		else:
			print("""
				Ошибка ввода! Введите название цвета или его RGB формат.
				ПРИМЕРЫ! test.draw_text("light blue") или test.draw_text(0, 255, 255)
				Для уточнения, какие цвета можно использовать, введите py.get_list_colors()
			""")
		