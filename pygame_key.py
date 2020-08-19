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

import mouse
import keyboard
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
	bot1 = Bot()

	while done:
		if pause_session:
			continue
		bot1.clear_pos_bot()
		bot1.draw_bot(x, y)

		x += math.sin(x) * 5
		y += -math.cos(y) * 5

		# если выход за пределы комнаты, то удаление
		if not py.check_object_on_screen((x, y)):
			bot1.clear_pos_bot()
			break

		bot1.set_color_bot(np.random.randint(140, 255), np.random.randint(140, 255), 255)
		bot1.draw_bot(x, y)
		py.update_screen()


num_index_list_bot = 3
# [id, x, y]
LIST_BOT = np.zeros((1, num_index_list_bot), dtype=int)  # Стиль имени!

# ?name
py = Drawing()
label_num_th = Text(y=15)
label_num_th.set_color_text("purple")
bool_mouse = Text(y=50)
bool_mouse.set_color_text("green")
bool_mouse_2 = Text(y=90)
bool_mouse_2.set_color_text("light blue")

done = True
pause_session = False

mouse_lbm = Event_mouse_and_keyboard()
keyboard_space = Event_mouse_and_keyboard()
keyboard_z = Event_mouse_and_keyboard()

# number_pix = np.ones((screen_width, screen_height), dtype=int)
# number_pix = np.zeros_like(number_pix)  # генерируем массив нулей (цвет чёрный)

# print(LIST_BOT)
x_old, y_old = mouse.get_position()
py.calibrate()
while done:
	# # # INFO # # #
	label_num_th.clear_text()
	bool_mouse.clear_text()
	bool_mouse_2.clear_text()
	py.update_screen()
	# Каждый поток - это бот. Поэтому рисуем количество ботов на экране, не считая главный поток, поэтому минус 1
	label_num_th.draw_text(threading.active_count()-1)
	# Рисуем позицию мыши
	# if py.check_border_screen(py.get_pos_mouse()):
	bool_mouse.draw_text(py.check_border_screen(mouse.get_position(), 14))
	bool_mouse_2.draw_text(mouse.get_position())
	
	# else:
	# 	bool_mouse.draw_text("False")
	# # # INFO # # #

	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			done = False

	keyboard_space.keyboard_pressed(pygame.K_SPACE, pause_ses)  # Стиль имени!
	keyboard_z.keyboard_pressed(pygame.K_z, closed_window)

	# width, height = py.get_size_window()
	if py.check_border_screen(mouse.get_position()) == 1 and mouse.is_pressed(button='left'):
		pass
	elif py.check_border_screen(mouse.get_position()) == 2 and mouse.is_pressed(button='left'):
		pass
	elif py.check_border_screen(mouse.get_position()) == 3 and mouse.is_pressed(button='left'):
		pass
	elif py.check_border_screen(mouse.get_position()) == 4 and mouse.is_pressed(button='left'):
		pass
	elif py.check_object_on_screen(py.get_pos_mouse()):
		mouse_lbm.mouse_pressed(0, start_th)
	# 	pause_session = True
	# 	while mouse.is_pressed(button='left'):
	# 		x_new, y_new = mouse.get_position()
	# 		delta_x = (x_old - x_new) #* 2
	# 		delta_y = (y_old - y_new) #* 2
	# 		print(delta_x, delta_y)
	# 		py.set_size_window(width - delta_x, height - delta_y)
	# 		time.sleep(0.1)
	# 		x_old, y_old = mouse.get_position()
	# 		time.sleep(0.1)
		
	# 	pause_session = False
		
	


	if pause_session:
		continue

	# pygame.draw.rect(window, (255, 255, 255), (45, 75, 10, 75))
	# pygame.draw.rect(window, (64, 128, 255), (150, 20, 100, 150), 4)
	
	py.update_screen_with_delay()
