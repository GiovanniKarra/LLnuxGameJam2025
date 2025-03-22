import asyncio
import websockets
from pickle import loads
from time import sleep
from freq import GameInstance, get_input_freq


async def client(server_ip, instance: GameInstance, port=8765):
	uri = f"ws://{server_ip}:{port}"
	async with websockets.connect(uri) as websocket:
		while True:
			sleep(1/30)
			message = str(get_input_freq())
			await websocket.send(message)
			response = await websocket.recv()
			response: GameInstance = loads(response)
			instance.freq_range = response.freq_range
			instance.max_time = response.max_time
			instance.players = response.players
			instance.rounds = response.rounds
			instance.scores = response.scores
			instance.target = response.target
			instance.timers = response.timers
			print(f"Server: {response}")

if __name__ == "__main__":
	server_ip = "0.0.0.0"
	# server_ip = input("Server IP: ")
	inst = GameInstance([])
	asyncio.run(client(server_ip, inst))