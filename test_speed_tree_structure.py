import time
import numpy as np

class Test():
	number_all_obj = 0

	def __init__(self):
		Test.number_all_obj += 1

	def get_id(self):
		return Test.number_all_obj

	def useful_work(self):
		time.sleep(0.01)

gen_obj = 14756

for i in range(gen_obj):
	space = Test()

list_divisors = [div for div in range (1, gen_obj // 2 + 1) if gen_obj % div == 0] + [gen_obj]
# print(list_divisors)

# start_time = time.time()
# end_time = time.time()
# delta = end_time - start_time
# print(delta)



rule = [2, 2, 2, 2]

tree = []
# for i in range(1, n + 1):
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
