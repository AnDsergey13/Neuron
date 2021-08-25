import time
import numpy as np


def gen_var(num_var):
	""" Генерим необходимое количество переменных с именами а1, а2, а3 ..."""
	for letter in range(1, num_var + 1):
		globals()[f"a{letter}"] = 0
		# Записываем названия в список, чтобы можно было обратиться
		list_name_var.append(f"a{letter}")
	
def get_name_var(index):
	return list_name_var[index]

def create_all_string(name_list, deep):
	""" Этот метод создаёт строку типа tree[a1][a2][a3]...
		Количество [] зависит от глубины списка. 
	"""

	# создаём основу строки для вставки в неё имён переменных
	# при глубине 4 будет tree[][][]
	# при глубине 2 будет tree[]
	string = name_list + "[]" * (deep - 1)

	# достаём имена переменных и вставляем с основную строку 
	for num_var in list_name_var[:-1]:
		string = string.replace("[]", f"[{num_var}]", 1)
	return string

def get_string(string, deep):
	# модифицируем строку, стобы проще было считать
	string += "["

	# Находим индекс [ , согласно глубине списка
	index = 0
	for i in range(deep):
		index = string.find('[', index + 1)

	# возвращаем обрезанную строку
	return string[:index]


rule = [2, 3, 4, 2]
tree = []
list_name_var = []

deep = len(rule)
# генерим необходимое количество переменных, и список имён этих перменных
gen_var(deep)
# создадим сначала полную строку, а после при необходимости будем её обрезать
string = create_all_string("tree", deep)

it = [1 for i in range(deep)]


for num_it in rule:
	while it[num_it] < rule[num_it]:
		# получаем обрезанную строку с необходимыми переменными
		# s = get_string(string, num_it + 1)
		# eval(s).append([])
		it[num_it] += 1
		print(it)



# print(tree)

# for a in range(rule[0]):
# 	tree.append([])

# 	for b in range(rule[1]):
# 		tree[a].append([])

# 		for c in range(rule[2]):
# 			tree[a][b].append([])

# 			for d in range(rule[3]):
# 				tree[a][b][c].append([])

# print(tree)

# for lvl_deep in range(deep):
# 	print(lvl_deep)
# 	gen_tree(lvl_deep)
# # print(list_name_var)
# # print(globals())
	

# for num_it in range(len(rule)):
# 	while it[num_it] < rule[num_it]:
# 		# получаем обрезанную строку с необходимыми переменными
#		# s = get_string(string, num_it + 1)
#		# eval(s).append([])
# 		it[num_it] += 1
# 		print(it)


# for num_vertical_it in rule:

# 	for num_horizontal_it in range(1, num_vertical_it + 1):

# 		print(num_vertical_it, num_horizontal_it)
# 		# it[num_it] += 1
# 		# print(it)


# def gen_tree(lvl_deep):
# 	# print(eval(get_name_var(lvl_deep)))
# 	x = eval(get_name_var(lvl_deep))
# 	for x in range(rule[lvl_deep]):
# 		# print(x)
# 		pass

# aa = [3]
# bb = aa
# print(aa, bb)
# aa[0] = 4
# print(aa, bb)
	
'''
eval("tree[0][1]").append('!!!')
print(tree)

def gen_names_variables(num_letters):
	""" Больше 26 переменных создать нельзя """
	result = ""
	if num_letters <= 26:
		for num_letter in range(97, 97 + num_letters):
			result += chr(num_letter)
	return result

# Количество уровней(слоёв) в древовидной структуре данных
deep_tree = 26

name_list = "tree"
square_brackets = "[]"
names_variable = gen_names_variables(deep_tree)

# создаём основу строки для вставки переменных
string = name_list + square_brackets * (deep_tree - 1)

# вставляем между квадратными скобками имя переменной
for letter in names_variable[1:]:
	string = string.replace("[]", f"[{letter}]", 1)
print(string)


def gen_loop(string):
	for b in range(rule[1]):
		eval(string).append([])
'''

"""

gen_obj = 14756

list_divisors = [div for div in range (1, gen_obj // 2 + 1) if gen_obj % div == 0] + [gen_obj]
# print(list_divisors)

# start_time = time.time()
# end_time = time.time()
# delta = end_time - start_time
# print(delta)s
"""