# Исправить паузу (не всегда срабатывает)
# БАГ. при создании, экземпляр не должен появляться на том месте, где уже есть экземпляр
# разделить отрисовку  и логику
# !добавить общий список, с координатами


import pygame
import time

import math
import numpy as np
import threading
		
def pause_ses():
	global pause_session
	pause_session = not pause_session
	print(pause_session)

def closed_window():
	global done
	done = False

def draw_num_th():
	# сначала закрасим текст черным (типа очистки), а потом отрисуем на нём количество активных потоков
	text1 = fontObj.render("█████", 1, (0, 0, 0),(0, 0, 0)) #alt + 219
	window. blit(text1, (10, 100))
	num_TH = str(threading.active_count())
	text1 = fontObj.render(num_TH, 1, (0, 255, 0))
	window. blit(text1, (10, 100))

def clear_bot(pix, x, y):
	"""заполнение чёрным там, где был бот"""
	pix. fill((0, 0, 0))
	window. blit(pix, (x, y))
	pygame. display. flip()

def key_pressed(mode, key_p, function):
	"""
	mode - режим клавиатура(0)/мышь(1)
	key_p - нажимаемая клавиша. клавиатура(pygame.K_SPACE)/мышь(ЛКМ(0),СКМ(1),ПКМ(2))
	function - запускаемая функция после события
	Example 1 (keyboard). key_pressed(0, pygame.K_SPACE, pause_ses)
	Example 2 (mouse). key_pressed(1, 0, closed)
	"""

	# Две отдельные функции, ибо клавиатура может работать вместе с мышью
	global block
	if mode == 0:	# клавиатура
		if pygame.key.get_pressed()[key_p] == 1:
			if block == False:
				# print("Кнопка на клавиатуре нажата")
				block = True
				function()
		else:
			block = False

	if mode == 1:	# мышь
		if pygame.mouse.get_pressed()[key_p] == 1:
			if block == False:
				# print("Кнопка мыши нажата")
				block = True
				function()
		else:
			block = False		

def start_th():
	create_bot = threading.Thread(target=create_object, args=(2,2,))
	# create_object(5,5)
	create_bot.start()

def create_object(x_scale = 1, y_scale = 1):
	global LIST_BOT 
	last_id = max(LIST_BOT.max(axis=1))
	current_id = last_id + 1

	(x, y) = pygame.mouse.get_pos()
	pix = pygame.Surface((x_scale, y_scale))

	draw_num_th()

	while done:
		if pause_session == True:
			continue
		clear_bot(pix, x, y)

		x += math.sin(x)*5
		y += -math.cos(y)*5
		# print(x,y)

		# если выход за пределы комнаты, то удаление
		if x > screen_width or x < 0 or y > screen_height or y < 0:
			clear_bot(pix, x, y)
			draw_num_th()
			break

		pix. fill((np.random.randint(140, 255), np.random.randint(140, 255), 255))
		window. blit(pix, (x, y))
		pygame. display. flip()

# [id, x, y]
LIST_BOT = np.zeros((3), dtype=int)


screen_width = 1000
screen_height = 500

speed = 100

pygame.init()
window = pygame.display.set_mode((screen_width , screen_height))
pygame.display.set_caption("Hello, pygame!")
fontObj = pygame.font.SysFont('verdana', 25)
pix = pygame.Surface((5, 5))

done = True
pause_session = False
block = False

number_pix = np.ones((screen_width , screen_height), dtype=int)
number_pix = np.zeros_like(number_pix) # генерируем массив нулей (цвет чёрный)

# print(LIST_BOT)

while done:
	for e in pygame.event.get() :
		if e. type == pygame. QUIT:
			done = False

	key_pressed(0, pygame.K_SPACE, pause_ses)
	key_pressed(0, pygame.K_z, closed_window)

	(x,y) = pygame.mouse.get_pos()
	if x > 0 and x < screen_width and y > 0 and y < screen_height:
		key_pressed(1, 0, start_th)


	if pause_session == True:
		continue

	pygame.draw.rect(window, (255, 255, 255), (45, 75, 10, 75))
	# pygame.draw.rect(window, (64, 128, 255), (150, 20, 100, 150), 4)
	



	pygame. display. flip()
	pygame.time.delay(speed)


# # генерация случайной позиции по х и по y
# 	# random.seed(5)
# 	x = np.random.randint(0, screen_width )
# 	y = np.random.razdint(0, screen_height)
# 	read_number = number_pix.take(x, axis=0)[y] # взятие числа в матрице по координатам 
# 	number_pix[x, y] = read_number + step	# увеличение яркости цвета на step(от чёрного к белому) при повторном попадании пикселя, на одно и тоже место
# 	if read_number > 255:
# 		pix. fill((255, 0, 255))
# 	else:
# 		pix. fill((read_number, read_number, read_number))

# 	window. blit(pix, (x, y))


#1
# x += int(x/y*4)
# y += int(y/x*4)
# #2
# x += x/100
# y += y/100
# #3?
# x += int(2-(math.sqrt(y)))
# y += int(2-(math.sqrt(x)))
# 4
# x += math.sin(x)*5
# y += -math.cos(y)*5
