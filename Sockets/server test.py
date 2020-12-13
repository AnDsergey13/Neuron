#https://realpython.com/python-sockets/
import socket
# import time
import threading


# поток для чтения с клавы. Чтобы не было ожидания ввода
def th_input_keyboard():
	global message
	while work_server:
		message = bytes(input(), 'utf-8')
	print("Прослушка клавы отключена")


def API():
	global work_server

	if data == b'password':
		conn.sendall(b"12345678")

	if data == b'end':
		conn.sendall(b"end")

	if data == b'0':
		print("Отключаем сервер")
		work_server = False


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 55555        # Port to listen on (non-privileged ports are > 1023)

work_server = True
message = b'1'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	print("Ждём подключения")
	conn, addr = s.accept()

	input_keyboard = threading.Thread(target=th_input_keyboard)
	input_keyboard.start()
	with conn:
		print('Connected by', addr)

		while work_server:
			data = conn.recv(1024)

			if data == b'end':
				work_server = False

			if not data == b'1':
				print("Принято ", data)
			# time.sleep(1)
			conn.sendall(message)
			if not message == b'1':
				print("Отправлено сообщение ", message)
				message = b'1'

			# API()

			# if not data:
			# 	work_server = False
