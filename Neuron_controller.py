from clNeuron import Space,Neuron
import numpy as np
import random
import time

def create_neuron():
	# for num in range(0, NUM_NEURONS):
	#	list_object.insert(num, n.Neuron())
	if len(list_object) < MAX_NEURONS:
		new_coord = gen_coord_neuron()
		for coord in list_coordinates:
			if new_coord == tuple(coord):
				#print("найдена копия, начинаем заново")
				break
		else:
			#print("копии нет, создаём нейрон")
			list_object.append(Neuron(space, new_coord[0], new_coord[1], new_coord[2]))
			list_coordinates.append([new_coord[0], new_coord[1], new_coord[2]])
	else:
		print("Привышено максимальное количество нейронов для данной области")
		
	

def gen_coord_neuron():
	mass = space.get_out_points()
	x = random.randrange(mass[0][0]+1, mass[2][0])
	y = random.randrange(mass[0][1]+1, mass[4][1])
	z = random.randrange(mass[0][2]+1, mass[1][2])
	return x, y, z

# def next(number_changes):
#     list_random_changes = [random.randrange(0, NUM_NEURONS) for i in range(number_changes)]
#     for num in list_random_changes:
#         list_object[num].next_step()

# def next_all():
#     for num in range(NUM_NEURONS):
#         list_object[num].next_step()

# def see_all_changes():
#     for num in range(len(list_object)):
#         print(f"{num}..{list_object[num].get_pos()}")

MAX_NEURONS = 100
list_object = []
list_coordinates = []

space = Space()
out_p = space.create_cube(10, 10, 10, size=20)
space.set_points(out_p, 1)
print(space.get_out_points())
print(space.get_in_points())

for i in range(100):
	create_neuron()
	print(len(list_object))
	#print(list_coordinates[i])
	#for neuron in list_object:
	#	print(neuron.get_pos())
#print(it)

# print(a.get_pos())
# print(a.is_internal_space())
# a.move(15, 25, 40)
# print(a.get_pos())
# print(a.is_internal_space())

# print("------------------")
# print(gen_coord_neuron())