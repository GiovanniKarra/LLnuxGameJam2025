import asyncio
import websockets


async def client(server_ip, port=8765):
	uri = f"ws://{server_ip}:{port}"
	async with websockets.connect(uri) as websocket:
		while True:
			message = input("Enter message: ")
			await websocket.send(message)
			response = await websocket.recv()
			print(f"Server: {response}")

if __name__ == "__main__":
	server_ip = "192.168.104.99"
	# server_ip = input("Server IP: ")
	asyncio.run(client(server_ip))