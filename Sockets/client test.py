import socket


def client_listen(client):
	global work_client
	
	while work_client:
		print("Ждём сообщения... \n ")
		data = client.recv(1024)

		if not data in list_command:
			print(f"Принято {data} \n ")
			

		if data == b"end":
			print("Клиент закрыт \n ")
			work_client = False
			client.close()

def Main():
	global work_client

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		client.connect((HOST, PORT))
		client_listen(client)
	except:
		print("Main. Ошибка при создании клиента \n")
		work_client = False
		client.close()

HOST = "127.0.0.1"
PORT = 13254

work_client = True
list_command = [b"end", b"close", b""]

Main()
