# -*- coding: utf-8 -

import sys
import threading

import keyboard
from websocket import create_connection


work_client = True


def emergency_shutdown():
	global work_client

	while work_client:
		if keyboard.is_pressed("/"):
			print("Активировано экстренное отключение")
			work_client = False
			ws.close()
			print("Закрываем клиент")
			sys.exit()


message = ""

ws = create_connection("ws://127.0.0.1:13254")
print("Подключился к серверу")

th_emergency_shutdown = threading.Thread(target=emergency_shutdown)
th_emergency_shutdown.start()

while work_client:
	message = input("Введите ваше сообщение")
	ws.send(message)
	print("Сообщение отправил, жду ответа...")

	result = ws.recv()
	print("Ответ '%s'" % result)
	if result == 'end':
		work_client = False

ws.close()
print("Клиент закрыт")
