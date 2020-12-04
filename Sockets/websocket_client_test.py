# -*- coding: utf-8 -
from websocket import create_connection


ws = create_connection("ws://127.0.0.1:13254")
print("Подключился к серверу")
ws.send("end")
print("Отвправил сообщение чтобы сервер закрылся")
print("Жду ответа...")
result =  ws.recv()
print("Ответ '%s'" % result)
ws.close()
print("Клиент закрыт")
