import socket
import asyncio

'''
ЗАДАЧИ
1) Узнать в чём ошибка у клиентов, когда одновременно закрываешь все соединения
Fatal Python error: could not acquire lock for <_io.BufferedWriter name='<stdout>'> at interpreter shutdown, possibly due to daemon threads
2) проверка на все возможные ошибки
3) избавится от потоков(асинхронность)
4) реализовать общий класс(?) для клиента и сервера
'''

# Сюда приходят команды из Debag.py(клавиатуры)
async def set_command(command):
	global message
	message = command

def shutdown_all_clients():
	# Отключение всех клиентов на стороне сервера
	for client in clients:
		try:
			client.close()
		except:
			print("shutdown_all_clients. Один из клиентов не может закрыться \n")
		
# ?????
async def client_send_message(server, conn# ?????):
	global work_server
	global message

	while work_server:
		if not message in list_command:
			try:
				await conn.send(message)
			except:
				print("client_send_message. Ошибка отправки сообщения \n")
				# Отключаем соединение для всех клиентов
				shutdown_all_clients()
				work_server = False
				server.shutdown(socket.SHUT_RDWR)
				server.close()
			message = b""

		if message == b"end":
			await conn.send(message)
			# Очищаем сообщение, чтобы условие больше не сработало
			message = b""
			# Удаляем из списка клиентов
			clients.remove(conn)
			conn.close()
			print("Отключаем клиента \n")
			# Без брейка поток продолжит отправлять данные на закрытый сокет
			break
		
# ?????
async def server_accept(server# ?????):
	global work_server

	while work_server:
		print("Сервер слушает ... ...")
		conn, _ = await server.accept()
		print(f"Подключился {conn}")
		clients.append(conn)


def create_server(HOST, PORT, NUM_CLIENTS):
	global work_server

	try:
		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind((HOST, PORT))
		server.listen(NUM_CLIENTS)
		server.setblocking(False)
		print("*** Сервер создан! ***")
		server_accept(server)
	except:
		work_server = False
		print("create_server. Ошибка при создании сервера \n")
		server.shutdown(socket.SHUT_RDWR)
		server.close()

	try:
		# ?????
		loop = asyncio.get_event_loop()
		loop.run_until_complete(run_server())
	except:
		print("create_server. Ошибка при создании списка событий \n")


HOST = "127.0.0.1"
PORT = 13254
NUM_CLIENTS = 5
clients = []

work_server = True
message = b""
list_command = [b"end", b"close", b""]

create_server(HOST, PORT, NUM_CLIENTS)