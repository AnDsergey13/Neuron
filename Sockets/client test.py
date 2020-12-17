import socket
import threading
import keyboard
import sys

def emergency_shutdown():
	global work_client

	while work_client:
		if keyboard.is_pressed("/"):
			print("\n Клиент - Активировано экстренное отключение \n ")
			work_client = False
			sys.exit()
	print("\n Поток emergency_shutdown - закрыт \n ")

'''
def input_keyboard():
	global message
	while work_client:
		message = bytes(input(), 'utf-8')
	print("Прослушка клавы отключена")
'''

def client_listen(client):
	global work_client
	
	while work_client:
		print("\n Ждём сообщения")
		data = client.recv(1024)

		if not data in list_command:
			print("\n Принято ", data)

		if data == b"end":
			print("\n Клиент закрыт")
			work_client = False

def Main():
	global work_client

	# Включаем поток для экстренного отключения клиента
	th_emergency_shutdown = threading.Thread(target=emergency_shutdown)
	# Завершить поток, если поток main завершится
	th_emergency_shutdown.daemon = True
	th_emergency_shutdown.start()

	try:
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.connect((HOST, PORT))
		client_listen(client)
	except:
		print("\n Main. Ошибка при создании клиента")
		work_client = False

HOST = "127.0.0.1"
PORT = 13254

work_client = True
list_command = ["end", "close", ""]

Main()
