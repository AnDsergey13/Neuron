# -*- coding: utf-8 -
from Keyboard_and_mouse import *

import math
import threading
import numpy as np
import time

import keyboard

size_x = 10
size_y = 10

c = Event("c")

# создаём поле
pole = np.ones((size_x, size_y), int)
# Заполняем поле нулями
pole.fill(0)

while not keyboard.is_pressed("space"):
	pass
	if c.is_keyboard_pressed():
		print(str(pole))

