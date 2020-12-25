import Sockets


def input_keyboard():
	while True:
		message = bytes(input("Введите сообщение: "), 'utf-8')

		if message == b"close":
			Sockets.set_command(message)
			print("!!! Клавиатура отключена !!!")
			break
		else: 
			Sockets.set_command(message)
			print(f"***Сообщение {message} отправлено")


input_keyboard()	
