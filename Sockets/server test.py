import socket
import threading


def input_keyboard():
	global message
	while work_server:
		message = bytes(input(), 'utf-8')
	print("\n Прослушка клавы отключена")

def client_send_message(conn):
	global work_server
	global message

	while work_server:
		if not message in list_command:
			try:
				conn.send(message)
			except:
				print("\n client_send_message. Ошибка отправки сообщения")
				work_server = False
			message = b""

		if message == b"end":
			conn.send(message)
			message = b""
			print("\n Отключаем клиента")
			# Без брейка поток продолжит отправлять данные на закрытый сокет
			break

		if message == b"close":
			conn.sendall(b"close")
			message = b""
			print("\n Получено сообщение выключение сервера")
			work_server = False

def server_accept(server):
	global work_server

	while work_server:
		print("\n Сервер слушает")
		conn, addr = server.accept()
		print(f"\n Подключился {conn} по адресу {addr}")
		clients.append(conn)

		try:
			# Создаём отдельны демон-потоки для клиентов
			th_cl_send_message = threading.Thread(target=client_send_message, args=(conn,))
			# Завершить поток, если поток main завершится
			th_cl_send_message.daemon = True
			th_cl_send_message.start()
		except:
			print("\n sever_accept. Ошибка при создании потока клиента")
			work_server = False

def Main():
	global work_server

	# Подключаем клавиатуру
	th_input_keyboard = threading.Thread(target=input_keyboard)
	# Завершить поток, если поток main завершится
	th_input_keyboard.daemon = True
	th_input_keyboard.start()

	try:
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind((HOST, PORT))
		server.listen(NUM_CLIENTS)

		server_accept(server)
	except:
		work_server = False
		print("Main. Ошибка при создании сервера")


HOST = "127.0.0.1"
PORT = 13254
NUM_CLIENTS = 5
clients = []

work_server = True
message = b""
list_command = [b"end", b"close", b""]

Main()