# https://www.youtube.com/watch?v=BmOjeVM0w1U

import asyncio
import keyboard
import sys

# Добавить пути и для винды и для линукса
sys.path.append('/home/pi/Documents/Python/Neuron')
from Keyboard_and_mouse import Event

delay = 1


async def banana():
	await asyncio.sleep(delay)
	print("Я люблю бананы")


async def apple():
	await asyncio.sleep(delay)
	print("Я люблю яблоки")


async def orange():
	await asyncio.sleep(delay)
	print("Я люблю апельсины")

fruits = [
	asyncio.ensure_future(banana()),
	asyncio.ensure_future(apple()),
	asyncio.ensure_future(orange())
]

event_loop = asyncio.get_event_loop()
# Добавляем в цикл список 
event_loop.run_until_complete(asyncio.gather(*fruits))
event_loop.close()
