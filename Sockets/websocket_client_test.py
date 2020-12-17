# -*- coding: utf-8 -
from websocket import create_connection
import threading
import keyboard
import sys

def wc_close():
	wc.close()
	print("Клиент закрыт")
	# sys.exit()


def emergency_shutdown():
	global work_client

	while work_client:
		if keyboard.is_pressed("/"):
			print("\nКлиент - Активировано экстренное отключение")
			work_client = False
	print("\n Поток emergency_shutdown - закрыт")
	wc_close()

work_client = True
result = ""

try:
	wc = create_connection("ws://127.0.0.1:13254")
	print("Подключился к серверу")
except:
	print("Ошибка подключения. Сервер недоступен")
	sys.exit()

th_emergency_shutdown = threading.Thread(target=emergency_shutdown)
th_emergency_shutdown.start()
# wc.send("Подключен")

while work_client:
	# БАГ. Если work_client изменится во время работы wc.recv(), то экстренного отключения не будет
	result =  wc.recv()
	if not result == "end":
		print("\nОтвет '%s'" % result)
		result = ""
		
	if result == "end":
		work_client = False

wc_close()


