import asyncio
import websockets
import time
from freq import GameInstance
from player import Player
from ascengine.core import Sprite
from pickle import dumps

HOST = "0.0.0.0"
PORT = 8765

instance = GameInstance([])
counter = 0

async def handle_client(websocket):
	"""Handles client messages and responds."""
	print(f"New connection from {websocket.remote_address}")
	global counter
	global instance
	counter += 1
	player_id = counter
	p = Player()
	p.set_id(player_id)
	p.set_sprite(Sprite("###\n###\n@%d@"%player_id))
	instance.players.append(p)
	try:
		t = time.perf_counter()
		async for message in websocket:
			print(f"Received: {message}")
			player_freq = float(message)
			p.set_freq(player_freq)
			new_t = time.perf_counter()
			instance.update(new_t-t)
			await websocket.send(dumps(instance))
			t = new_t
	except:
		print("Client disconnected")
		instance.players.remove(p)

async def main():
	server = await websockets.serve(handle_client, HOST, PORT)
	print(f"WebSocket server started on {HOST}:{PORT}")
	await server.wait_closed()

if __name__ == "__main__":
	asyncio.run(main())