# разделить класс Drawing на подклассы 
# БАГ. при создании, экземпляр не должен появляться на том месте,
#     где уже есть экземпляр
# !добавить общий список, с координатами

from Keyboard_and_mouse import Event_mouse_and_keyboard
from Drawing import Drawing

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
	global done
	done = False


def start_th():
	create_bot = threading.Thread(target=create_object)
	# create_object(5, 5)
	create_bot.start()


def create_object():
	global LIST_BOT

	last_id = max(LIST_BOT.take(1, axis=1))
	current_id = last_id + 1
	LIST_BOT = np.append(
		LIST_BOT,
		np.zeros((1, num_index_list_bot), dtype=int),
		axis=0)

	# ???
	x, y = py.get_pos_mouse()
	py.create_bot(3, 3)

	while done:
		if pause_session:
			continue
		py.clear_pos_bot()
		py.draw_bot(x, y)

		x += math.sin(x) * 5
		y += -math.cos(y) * 5

		# если выход за пределы комнаты, то удаление
		if not py.check_object_on_screen((x, y)):
			py.clear_pos_bot()
			break

		py.set_color_bot(np.random.randint(140, 255), np.random.randint(140, 255), 255)
		py.draw_bot(x, y)
		py.update_screen()


num_index_list_bot = 3
# [id, x, y]
LIST_BOT = np.zeros((1, num_index_list_bot), dtype=int)  # Стиль имени!

# ?name
py = Drawing()

done = True
pause_session = False

mouse_lbm = Event_mouse_and_keyboard()
keyboard_space = Event_mouse_and_keyboard()
keyboard_z = Event_mouse_and_keyboard()

# number_pix = np.ones((screen_width, screen_height), dtype=int)
# number_pix = np.zeros_like(number_pix)  # генерируем массив нулей (цвет чёрный)

# print(LIST_BOT)

while done:
	py.clear_text()
	py.update_screen()
	# рисуем количество потоков
	py.draw_text("purple", value=threading.active_count())

	print(threading.active_count())
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			done = False

	keyboard_space.keyboard_pressed(pygame.K_SPACE, pause_ses)  # Стиль имени!
	keyboard_z.keyboard_pressed(pygame.K_z, closed_window)

	if py.check_object_on_screen(py.get_pos_mouse()):
		mouse_lbm.mouse_pressed(0, start_th)

	if pause_session:
		continue

	# pygame.draw.rect(window, (255, 255, 255), (45, 75, 10, 75))
	# pygame.draw.rect(window, (64, 128, 255), (150, 20, 100, 150), 4)
	
	py.update_screen_with_delay()
