# -*- coding: utf-8 -

# ЗАДАЧИ
# Реализовать полудуплекную связь
# Баг! Сервер не отключается. (Гипотеза - потоки в библиотеке)
#
#

from websocket_server import WebsocketServer
import threading
import keyboard
import sys


def emergency_shutdown():
	while True:
		if keyboard.is_pressed("."):
			print("Сервер - активировано экстренное отключение!")
			server.server_complete()
			print("Закрываем сервер")
			sys.exit()

def loop(client, server, message):

	if not message == "end":
		print("Пришло сообщение {} от {}".format(message, client))
		server.send_message(client, "Ответ = {}".format(message))
		print("Ответ оправлен")

	if message == "end":
		print("Получено сообщение выключение сервера")
		server.send_message_to_all("end")
		server.server_complete() # Отключение сервера 
		print("Сервер отключён")
		sys.exit()

	# server.send_message_to_all("Hey all, a new client has joined us")

server = WebsocketServer(13254, host='127.0.0.1')

th_emergency_shutdown = threading.Thread(target=emergency_shutdown)
th_emergency_shutdown.start()

server.set_fn_message_received(loop)
print("Сервер запущен")
server.run_forever()
print("файл закрыт")
