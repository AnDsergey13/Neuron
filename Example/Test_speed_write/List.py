import time
import statistics

global_start_time = time.time()

ITER = 1000000
REPEAT = 10
delta = []
temp = []

def write_data():
    global temp
    start_time = int(time.time()*1000000)
    for i in range(ITER):
        temp.append(i)
    end_time = int(time.time()*1000000)
    return start_time, end_time

for repeat in range(REPEAT):
    r = write_data()
    delta.append(r[1] - r[0])
    print(f"{repeat}..{r[1]} - {r[0]} = {delta[repeat]}")
    
print(f"Среднее время работы = {statistics.median(delta)/1000000} секунд")
global_end_time = time.time()
print(f"Общее время работы программы = {global_end_time - global_start_time} секунд")
