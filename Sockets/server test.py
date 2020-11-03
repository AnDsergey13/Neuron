#https://realpython.com/python-sockets/
import socket
import time
import threading

def th_input_keyboard():
	global message
	# поток для чтения с клавы. Чтобы не было ожидания ввода
	message = bytes(input(), 'utf-8')
	# conn.sendall(bytes(input(), 'utf-8'))

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
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

work_server = True
message = b''

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	
	s.listen()
	print("Ждём подключения")
	conn, addr = s.accept()
	with conn:
		print('Connected by', addr)
		
		while work_server:
			data = conn.recv(1024)
			print(data)

			th_input_keyboard()
			
			API()

			if not data:
				break
