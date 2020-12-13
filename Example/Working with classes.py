# import pygame

# class Event_mouse_and_keyboard():
class Operation():
	""" +++Класс для теста+++ """
	acceptable_structures = ["<class 'list'>", "<class 'tuple'>"]

	# при созданиии объекта класса, автоматически запускается этот метод
	def __init__(self, name="-Никто-", block=0):
		""" +++Автоматически запускаем метод+++
		Пример:
		name - это имя объекта
		block - печать имени(1 - не печатает, 0 - печатает)
		Operation("Эдвард", 1)"""
		# печатаем имя, только тогда когда нужно программисту
		if block == 0:
			print(f"Объект c именем -{name}- создан!")
		self.names = name

	# без self метод класса не вызовется
	# после self, пишутся поля(переменные), которые передаются в метод
	def output(self, value):
		""" +++Вывод введённого значения+++ """
		print("Вы ввели = ", value)
		pass

	def test_data(self, data):
		""" При вызове метода класса, передаваемые данные заворачиваются в кортеж.
			Следующим действием проверяем, есть ли в кортеже другие структуры.
			И если есть, то убираем его.
		"""

		if len(data) == 1:
			data = data[0]
		return data

	def plus(self, *numbers):
		""" +++ Операция сложения только для чисел, кортежей и списков +++ """

		# убираем внешний кортеж, если нужно
		numbers = self.test_data(numbers)

		summ = 0
		# перебираем по допустимым структурам
		# сложение элементов в списке или кортеже
		for type_structures in Operation.acceptable_structures:
			if str(type(numbers)) == type_structures:
				for number in numbers:
					summ += number
				return summ

		print("Введите допустимый тип аргумента. Список, число или кортеж")

	def minus(self):
		""" +++Операция вычитания+++ """
		# print("Операция вычитания")
		# print(self.name)
		return self.names


# изучение наследования
class podClass(Operation):
	""" DOC """

	def __init__(self):
		""" DOC """
		print("Подкласс запустился")

	def metod1(self):
		""" DOC """
		pass


# num_bananes = Operation("Объект 1", 1)
cheburek = podClass()
# вызывается ошибка так как переменная self.names не создавалась в podClass
print(cheburek.minus())
# help(num_bananes)

# print(num_bananes.output.__doc__)
# num_bananes.output(5)

# mass = {5, 7643, 975, 7748}
# print(num_bananes.plus(5, 7643, 975, 7748))
# print(num_bananes.plus(mass))

# print(num_bananes.minus())
