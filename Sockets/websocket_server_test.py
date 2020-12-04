# -*- coding: utf-8 -
from websocket_server import WebsocketServer

def loop(client, server, message):

	if message == "end":
		print("Получено сообщение выключение сервера")
		server.send_message(client, "Сервер работает")
		server.server_complete() # Отключение сервера 
		print("Сервер отключён")

	# server.send_message_to_all("Hey all, a new client has joined us")

server = WebsocketServer(13254, host='127.0.0.1')
server.set_fn_message_received(loop)
print("Сервер запущен")
server.run_forever()
print("файл закрыт")
