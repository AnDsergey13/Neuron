#https://realpython.com/python-sockets/
import socket
import time
import threading

# поток для чтения с клавы. Чтобы не было ожидания ввода
def th_input_keyboard():
	global message
	while work_client:
		message = bytes(input(), 'utf-8')
	print("Прослушка клавы отключена")

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 55555        # The port used by the server

work_client = True
message = b'1'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))

	input_keyboard = threading.Thread(target=th_input_keyboard)
	input_keyboard.start()

	while work_client:
		s.sendall(message)

		if message == b'end':
			work_client = False

		if not message == b'1':
			print("Отправлено сообщение ", message)
			message = b'1'
		time.sleep(0.1)

		data = s.recv(1024)
		if not data == b'1':
				print("Принято ", data)
		
		# if data == b'end':
		# 	print("Клиент закрыт")
		# 	work_client = False

	

# print('Received', repr(data))