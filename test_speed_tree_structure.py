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



n = 8
rule = [2, 3]

list_o = []
for i in range(1, n + 1):
	print(i)
