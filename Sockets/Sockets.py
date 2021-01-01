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

'''
# Сюда приходят команды из Debag.py(клавиатуры)
async def set_command(command):
	global message
	message = command
'''

def shutdown_all_clients():
	# Отключение всех клиентов на стороне сервера
	for client in clients:
		try:
			client.close()
		except:
			print("shutdown_all_clients. Один из клиентов не может закрыться \n")


async def client_send_message(loop, server, client):
	global work_server
	global message

	for i in range(300):
		await loop.sock_sendall(client, str(i).encode())
		await asyncio.sleep(0.1)
	clients.remove(client)
	await loop.sock_sendall(client, b"end")
	client.close()
	print("Отключаем клиента \n")

	"""
	while work_server:
		
		if not message in list_command:
			try:
				await loop.sock_send(client, message)
			except:
				print("client_send_message. Ошибка отправки сообщения \n")
				# Отключаем соединение для всех клиентов
				shutdown_all_clients()
				work_server = False
				server.shutdown(socket.SHUT_RDWR)
				server.close()
			message = b""

		if message == b"end":
			await loop.sock_send(client, message)
			# Очищаем сообщение, чтобы условие больше не сработало
			message = b""
			# Удаляем из списка клиентов
			clients.remove(client)
			print("Отключаем клиента \n")
			# Без брейка поток продолжит отправлять данные на закрытый сокет
			break
		
	client.close()"""


async def server_accept(loop, server):
	global work_server

	while work_server:
		client, _ = await loop.sock_accept(server)
		print(f"Подключился {client}")
		loop.create_task(client_send_message(loop, server, client))

		clients.append(client)


def create_server():
	global work_server

	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		server.bind((HOST, PORT))
		server.listen(NUM_CLIENTS)
		server.setblocking(False)
		print("*** Сервер создан! ***")
	except:
		print("create_server. Ошибка при настройке сервера \n")
		server.shutdown(socket.SHUT_RDWR)
		server.close()

	try:
		loop = asyncio.get_event_loop()
		loop.run_until_complete(server_accept(loop, server))
	except:
		work_server = False
		print("create_server. Ошибка при создании списка событий \n")
		server.shutdown(socket.SHUT_RDWR)
		server.close()


HOST = "127.0.0.1"
PORT = 13254
NUM_CLIENTS = 5
clients = []

work_server = True
message = b""
list_command = [b"end", b"close", b""]

if __name__ == "__main__":
	create_server()