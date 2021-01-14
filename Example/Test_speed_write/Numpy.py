import time
import numpy as np

global_start_time = time.time()

ITER = 1000000
REPEAT = 10
delta = np.empty((1, REPEAT),'int')
temp = np.empty((1, ITER*REPEAT),'int')

def write_data():
    global temp
    start_time = int(time.time()*1000000)
    for i in range(ITER):
        temp[0][i] = i
    end_time = int(time.time()*1000000)
    return start_time, end_time

for repeat in range(REPEAT):
    r = write_data()
    delta[0][repeat] = r[1] - r[0]
    print(f"{repeat}..{r[1]} - {r[0]} = {delta[0][repeat]}")

print(f"Среднее время работы = {delta.mean()/1000000} секунд")
global_end_time = time.time()
print(f"Общее время работы программы = {global_end_time - global_start_time} секунд")
