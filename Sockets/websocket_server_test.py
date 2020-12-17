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

def server_close():
	server.shutdown()
	print("\n Сервер отключён")
	sys.exit()

def input_keyboard():
	global work_server
	global message

	while work_server:
		message = input("\nВведите ваше сообщение: ")
		if message == "close":
			work_server = False
		if message == "red":
			server.send_message_to_all(message)
			message = ""
	print("\nПрослушка клавы отключена")

def emergency_shutdown():
	global work_server
	while work_server:
		if keyboard.is_pressed("."):
			print("\nСервер - активировано экстренное отключение!")
			work_server = False
		
	print("\n Поток emergency_shutdown - закрыт")
	server_close()

def loop(client, server, msg):

	if not message in list_command:
		server.send_message_to_all(message)
		message = ""

	if message == "end":
		message = ""
		server.send_message_to_all("end")
		print("Отключаем всех клиентов")

	if message == "close":
		print("Получено сообщение выключение сервера")
		server.send_message_to_all("end")
		server_close()
		sys.exit()

	# server.send_message_to_all("Hey all, a new client has joined us")


def new_client(client, server):
	id_client = dict(client)["id"]
	ip_port = dict(client)["address"]
	format_ip_port = "{}:{}".format(str(ip_port[0]), str(ip_port[1]))
	print("\nПодключился клиент {} с адресом {}".format(id_client, format_ip_port))

'''
def loop():
	global message

	while work_server:
		if not message in list_command:
			server.send_message_to_all(message)
			message = ""

		if message == "end":
			message = ""
			server.send_message_to_all("end")
			print("Отключаем всех клиентов")

		if message == "close":
			print("Получено сообщение выключение сервера")
			server.send_message_to_all("end")
			server_close()
			sys.exit()
	

	# server.send_message_to_all("Hey all, a new client has joined us")
'''
list_command = ["end", "close", ""]

work_server = True
message = ""


server = WebsocketServer(13254, host='127.0.0.1')

th_emergency_shutdown = threading.Thread(target=emergency_shutdown)
th_emergency_shutdown.start()
th_input_keyboard = threading.Thread(target=input_keyboard)
th_input_keyboard.start()

server.set_fn_message_received(loop)
server.set_fn_new_client(new_client)
print("Сервер запущен")
# loop()
server.run_forever()
print("файл закрыт")
