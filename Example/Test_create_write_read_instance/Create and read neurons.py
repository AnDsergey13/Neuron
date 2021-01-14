import Test_class_neuron as n
import random
import time

NUM_NEURONS = 1000000
list_object = []

def print_time(start_time, end_time):
    delta = end_time - start_time
    print(f"{end_time} - {start_time} = {delta}")

def create():
    global list_object

    start_time = time.time()
    for num in range(0, NUM_NEURONS):
        list_object.insert(num, n.Neuron())

    end_time = time.time()
    print_time(start_time, end_time)


def next(number_changes):
    start_time = time.time()

    list_random_changes = [random.randrange(0, NUM_NEURONS) for i in range(number_changes)]
    for num in list_random_changes:
        list_object[num].next_step()

    end_time = time.time()
    print_time(start_time, end_time)

def next_all():
    start_time = time.time()

    for num in range(NUM_NEURONS):
        list_object[num].next_step()

    end_time = time.time()
    print_time(start_time, end_time)

def see_all_changes():
    start_time = time.time()

    for num in range(len(list_object)):
        print(f"{num}..{list_object[num].get_pos()}")

    end_time = time.time()
    print_time(start_time, end_time)

create()
next_all()
#next(100000)
#see_all_changes()