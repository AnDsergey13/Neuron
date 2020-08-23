# БАГ. При остановки программы, пропадает текст на экране
# сделать гибкое изменение размера экрана
# БАГ. при создании, экземпляр не должен появляться на том месте,
#     где уже есть экземпляр
# !добавить общий список, с координатами

from Keyboard_and_mouse import Event_mouse_and_keyboard
from Drawing import *

import math
import time
import threading

import pygame
import numpy as np


def pause_ses():
	global pause_session
	pause_session = not pause_session
	print(pause_session)


def closed_window():





	global on
	on = False


num_index_list_bot = 3
# [id, x, y]
LIST_BOT = np.zeros((1, num_index_list_bot), dtype=int)  # Стиль имени!

# ?name
py = Drawing()
label_num_th = Text(y=15)
label_num_th.set_color_text("purple")
bool_mouse = Text(y=50)
bool_mouse.set_color_text("green")

on = True
pause_session = False

lbm = Event_mouse_and_keyboard()
space = Event_mouse_and_keyboard()
z = Event_mouse_and_keyboard()

# number_pix = np.ones((screen_width, screen_height), dtype=int)
# number_pix = np.zeros_like(number_pix)  # генерируем массив нулей (цвет чёрный)

# print(LIST_BOT)

while on:
	# # # INFO # # #
	label_num_th.clear_text()
	bool_mouse.clear_text()
	py.update_screen()
	# Каждый поток - это бот. Поэтому рисуем количество ботов на экране, не считая главный поток, поэтому минус 1
	label_num_th.draw_text(threading.active_count()-1)
	# Рисуем позицию мыши
	bool_mouse.draw_text(py.get_pos_mouse())

	# # # INFO # # #

	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			done = False


	if py.check_object_on_screen(py.get_pos_mouse()):
		lbm.mouse_pressed(0, Neuron_)

	if space.is_keyboard_pressed(pygame.K_SPACE):
		set_pause_session()

	if z.is_keyboard_pressed(pygame.K_z):
		neuron_off()
		closed_window()
	if pause_session:
		continue

	# pygame.draw.rect(window, (255, 255, 255), (45, 75, 10, 75))
	# pygame.draw.rect(window, (64, 128, 255), (150, 20, 100, 150), 4)
	
	py.update_screen_with_delay()
