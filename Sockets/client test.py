import socket
import threading
import keyboard
import sys

def emergency_shutdown(client):
	global work_client

	while work_client:
		if keyboard.is_pressed("/"):
			print("Клиент - Активировано экстренное отключение \n ")
			client.close()
			work_client = False
			sys.exit()
	print("Поток emergency_shutdown - закрыт \n ")

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
		print("Ждём сообщения... \n ")
		data = client.recv(1024)

		if not data in list_command:
			print(f"Принято {data} \n ")
			data = b""
			

		if data == b"end":
			print("Клиент закрыт \n ")
			work_client = False
			client.close()

def Main():
	global work_client

	try:
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.connect((HOST, PORT))

		# Включаем поток для экстренного отключения клиента
		th_emergency_shutdown = threading.Thread(target=emergency_shutdown, args=(client,))
		# Завершить поток, если поток main завершится
		th_emergency_shutdown.daemon = True
		th_emergency_shutdown.start()
			
		client_listen(client)
	except:
		print("Main. Ошибка при создании клиента \n")
		work_client = False
		client.close()

HOST = "127.0.0.1"
PORT = 13254

work_client = True
list_command = ["end", "close", ""]

Main()
