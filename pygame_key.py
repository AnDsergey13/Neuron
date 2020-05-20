import pygame
import numpy as np
import time
import threading
		
def pause_ses():
	global pause_session
	pause_session = not pause_session
	print(pause_session)

def closed():
	global done
	done = False

def key_pressed(mode, key_p, function):
	"""
	mode - режим клавиатура(0)/мышь(1)
	key_p - нажимаемая клавиша. клавиатура(pygame.K_SPACE)/мышь(ЛКМ(0),СКМ(1),ПКМ(2))
	function - запускаемая функция после события
	Example 1 (keyboard). key_pressed(0, pygame.K_SPACE, pause_ses)
	Example 2 (mouse). key_pressed(1, 0, closed)
	"""

	global block
	if mode == 0:	# клавиатура
		if pygame.key.get_pressed()[key_p] == 1:
			if block == False:
				print("Кнопка на клавиатуре нажата")
				block = True
				function()
		else:
			block = False

	if mode == 1:	# мышь
		if pygame.mouse.get_pressed()[key_p] == 1:
			if block == False:
				print("Кнопка мыши нажата")
				block = True
				function()
		else:
			block = False		

def create_object(x_scale = 1, y_scale = 1):
	print(threading.active_count())
	(x, y) = pygame.mouse.get_pos()
	pix = pygame.Surface((x_scale, y_scale))
	# bot(pix, x, y)
	while done:
		if pause_session == True:
			continue
		pix. fill((0, 0, 0))
		window. blit(pix, (x, y))
		pygame. display. flip()
		x += np.random.randint(-1, 1)
		y += np.random.randint(-1, 1)
		pix. fill((np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)))
		window. blit(pix, (x, y))
		pygame. display. flip()

		# выход за пределы комнаты
		if x > x_ or x < 0 or y > y_ or y < 0:
			# запонение чёрным, где был бот
			pix. fill((0, 0, 0))	
			window. blit(pix, (x, y))
			pygame. display. flip()

			print("del_bot")
			break

# def bot(pix, x, y):
# 	while done:
# 		x += np.random.randint(-5, 5)
# 		y += np.random.randint(-5, 5)
# 		pix. fill((0, 255, 0))
# 		window. blit(pix, (x, y))
# 		pygame. display. flip()
# 		# pygame.time.delay(10)

def TH_start():
	create_bot = threading.Thread(target=create_object, args=(1,1,))
	# create_object(5,5)
	create_bot.start()

def num_th():
	print(threading.active_count())

x_ = 1200
y_ = 768

speed = 0
step = 25

window = pygame.display.set_mode((x_, y_))
pygame.display.set_caption("Hello, pygame!")
pix = pygame.Surface((5, 5))
done = True

pause_session = False
block = False

number_pix = np.ones((x_, y_), dtype=int)
number_pix = np.zeros_like(number_pix) # геренрируем массив нулей(цвет чёрный)

while done:
	for e in pygame.event.get() :
		if e. type == pygame. QUIT:
			done = False

	key_pressed(0, pygame.K_SPACE, pause_ses)
	key_pressed(0, pygame.K_z, closed)
	key_pressed(0, pygame.K_x, num_th)	#показать количество запущенных потоков

	key_pressed(1, 0, TH_start)

	fontObj = pygame.font.SysFont(None, 36)
	text1 = fontObj.render('Hello Привет', 1, (180, 0, 0))
	window. blit(text1, (10, 100))


	# print(pygame.mouse.get_pressed()[0])

	# if pygame.mouse.get_pressed()[0] == 1:
	# 	create_bot = threading.Thread(target=create_object, args=(5,5,))
	# 	# create_object(5,5)
	# 	create_bot.start()

	if pause_session == True:
		continue




	pygame. display. flip()
	pygame.time.delay(speed)


# # генерация случайной позиции по х и по y
# 	# random.seed(5)
# 	x = np.random.randint(0, x_)
# 	y = np.random.razdint(0, y_)
# 	read_number = number_pix.take(x, axis=0)[y] # взятие числа в матрице по координатам 
# 	number_pix[x, y] = read_number + step	# увеличение яркости цвета на step(от чёрного к белому) при повторном попадании пикселя, на одно и тоже место
# 	if read_number > 255:
# 		pix. fill((255, 0, 255))
# 	else:
# 		pix. fill((read_number, read_number, read_number))

# 	window. blit(pix, (x, y))