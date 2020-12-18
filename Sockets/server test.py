import socket
import threading
'''
ЗАДАЧИ
1) Узнать в чём ошибка у клиентов, когда одновременно закрываешь все соединения
Fatal Python error: could not acquire lock for <_io.BufferedWriter name='<stdout>'> at interpreter shutdown, possibly due to daemon threads
2) проверка на все возможные ошибки
3) избавится от потоков(асинхронность)
4) реализовать общий класс(?) для клиента и сервера
'''


def shutdown_clients_emergency():
	# Имя?
	# Отключение клиентов на стороне сервера
	for client in clients:
		try:
			client.close()
		except:
			print("shutdown_clients_emergency. Один из клиентов не может закрыться \n")
	

def input_keyboard(server):
	global message
	global work_server

	while work_server:
		message = bytes(input(), 'utf-8')

		if message == b"close":
			print("Получено сообщение выключение сервера \n")
			message = b""
			shutdown_clients_emergency()
			server.shutdown(socket.SHUT_RDWR)
			work_server = False
			server.close()
	print("Поток input_keyboard - закрыт \n")		

def client_send_message(server, conn):
	global work_server
	global message

	while work_server:
		if not message in list_command:
			try:
				conn.send(message)
			except:
				print("client_send_message. Ошибка отправки сообщения \n")
				# Отключаем соединение для всех клиентов
				shutdown_clients_emergency()
				work_server = False
				server.shutdown(socket.SHUT_RDWR)
				server.close()
			message = b""

		if message == b"end":
			# Отправляем сообщение, чтобы клиент закрывался
			shutdown_clients_emergency()
			# Очищаем сообщение, чтобы условие больше не сработало
			message = b""
			# Удаляем из списка клиентов
			clients.remove(conn)
			print("Отключаем клиента \n")
			# Без брейка поток продолжит отправлять данные на закрытый сокет
			break

def server_accept(server):
	global work_server

	while work_server:
		print("Сервер слушает \n")
		conn, addr = server.accept()
		print(f"Подключился {conn} по адресу {addr} \n")
		clients.append(conn)

		try:
			# Создаём отдельны демон-потоки для клиентов
			th_cl_send_message = threading.Thread(target=client_send_message, args=(server, conn,))
			# Завершить поток, если поток main завершится
			th_cl_send_message.daemon = True
			th_cl_send_message.start()
		except:
			print("sever_accept. Ошибка при создании потока клиента \n")
			work_server = False
			server.shutdown(socket.SHUT_RDWR)
			server.close()

def Main():
	global work_server

	try:
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		# Подключаем клавиатуру
		th_input_keyboard = threading.Thread(target=input_keyboard, args=(server,))
		# Завершить поток, если поток main завершится
		th_input_keyboard.daemon = True
		th_input_keyboard.start()

		server.bind((HOST, PORT))
		server.listen(NUM_CLIENTS)

		server_accept(server)
	except:
		work_server = False
		print("Main. Ошибка при создании сервера \n")
		server.shutdown(socket.SHUT_RDWR)
		server.close()


HOST = "127.0.0.1"
PORT = 13254
NUM_CLIENTS = 5
clients = []

work_server = True
message = b""
list_command = [b"end", b"close", b""]

Main()