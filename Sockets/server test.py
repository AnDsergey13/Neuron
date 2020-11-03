#https://realpython.com/python-sockets/
import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	
	s.listen()
	print("Сокет слушает")
	conn, addr = s.accept()
	print("Ждём подключения")
	with conn:
		print('Connected by', addr)
		while True:
			data = conn.recv(1024)
			print(data)
			# поток для чтения с клавы. Чтобы не было ожидания ввода
			conn.sendall(bytes(input(), 'utf-8'))
			
			if data == b'password':
				conn.sendall(b"12345678")

			if data == b'end':
				conn.sendall(b"end")

			if data == b'0':
				print("Отключаем сервер")
				break

			
			if not data:
				break
