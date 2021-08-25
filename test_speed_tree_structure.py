import time
import numpy as np
import copy

gen_obj = 14756

list_divisors = [div for div in range (1, gen_obj // 2 + 1) if gen_obj % div == 0] + [gen_obj]
# print(list_divisors)

# start_time = time.time()
# end_time = time.time()
# delta = end_time - start_time
# print(delta)

rule = [2, 3, 4, 2]

tree = []
list_name_var = []

def gen_var(num_var):
	""" Генерим необходимое количество переменных с именами а1, а2, а3 ..."""
	for letter in range(1, num_var + 1):
		globals()[f"a{letter}"] = 0
		# Записываем названия в список, чтобы можно было обратиться
		list_name_var.append(f"a{letter}")
	
def get_name_var(index):
	return list_name_var[index]

def gen_tree(lvl_deep):
	# print(eval(get_name_var(lvl_deep)))
	x = eval(get_name_var(lvl_deep))
	for x in range(rule[lvl_deep]):
		#print(x)
		pass



deep = len(rule)
gen_var(deep)

for lvl_deep in range(deep):
	gen_tree(lvl_deep)
# print(list_name_var)
# print(globals())

aa = 3
bb = copy.deepcopy(aa)
print(aa, bb)
aa = 4
print(aa, bb)


'''
for a in range(rule[0]):
	tree.append([])

	for b in range(rule[1]):
		tree[a].append([])

		for c in range(rule[2]):
			tree[a][b].append([])

			for d in range(rule[3]):
				tree[a][b][c].append([])

print(tree)	

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