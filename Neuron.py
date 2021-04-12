import random

class Neuron():
	def __init__(self, obj_space, x=25, y=25, z=25):
		#self.list_input = []
		#self.list_output = []
		self.obj_space = obj_space

		self.x_pos = x
		self.y_pos = y
		self.z_pos = z

		new_pos = self.calc_new_pos()
		self.set_pos(new_pos)

		# По умолчанию состояние равно 0
		self.set_state(0)

	def set_pos(self, xyz):
		# 1. Проверка, нужно ли нейрону вообще передвигаться
		# 2. Получить координаты и состояния всех ближайших нейронов
		# 3. Вычислить точку для передвижения
		# 4. Проверить, сможет ли нейрон перейти в новую точку
		# 5. Если да, то двигаем self.calc_new_pos(x, y, z)
		# 6. Если нет, то старт с п.3.

		# Перед перемещением нейрона проверяем, не выйдет ли он за границу внешней области
		if self.is_space(xyz, "out"):
			self.x_pos, self.y_pos, self.z_pos = xyz

	def calc_new_pos(self):
		x_pos = self.x_pos + random.randrange(-1, 2)
		y_pos = self.y_pos + random.randrange(-1, 2)
		z_pos = self.z_pos + random.randrange(-1, 2)
		return x_pos, y_pos, z_pos

	def get_pos(self):
		return self.x_pos, self.y_pos, self.z_pos

	def set_state(self, state):
		"""	set_state(self, state). 
			Устанавить 1 из 6 состояний нейрона.
				state(int) - номер состояния, где:
					0 - нейрон ищущий подключения в локальном пространстве. Динамичен
					1 - нейрон, с неполным подключением(без сети). Ожидает других подключений. Статичен
					2 - нейрон, с неполным подключением через сеть. Ожидает других подключений. Статичен
					3 - нейрон, с полным подключением(без сети). Ничего не ожидает. Статичен
					4 - нейрон, с полным подключением через сеть. Ничего не ожидает. Статичен
					5 - это смерть нейрона. Ожидает уничтожения
		"""
		self.state = state

	def get_state(self):
		"""
			Возвращает номер состояния указанного нейрона
		"""
		return self.state

	def is_space(self, xyz=None, mode="in"):
		""" 
		is_space(xyz=None, mode="in")

		Возвращает True, если нейрон находится в указанной области пространства.

		По умолчанию, mode="in" - это внутренняя область, 
		а mode="out" - это внешняя область.

		xyz - По умолчанию, берёт координаты текущего нейрона. 
		Принимает в себя кортеж или список координат объекта, для проверки. Пример записи: (34, -56, 1)

		"""
		if xyz == None:
			x, y, z = self.x_pos, self.y_pos, self.z_pos
		else:
			x, y, z = xyz

		if mode == "in":
			space = self.obj_space.get_in_points()
		elif mode == "out":
			space = self.obj_space.get_out_points()
		else:
			print("***** Не верно указано название пространства. Установлено по умолчанию. in")
			space = self.obj_space.get_in_points()


		delta_x = x > space[0][0] and x < space[2][0]
		delta_y = y > space[0][1] and y < space[4][1]
		delta_z = z > space[0][2] and z < space[1][2]

		return delta_x and delta_y and delta_z

