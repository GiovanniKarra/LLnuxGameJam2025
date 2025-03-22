import asyncio
import websockets

HOST = "0.0.0.0"
PORT = 8765

async def handle_client(websocket):
	"""Handles client messages and responds."""
	print(f"New connection from {websocket.remote_address}")

	try:
		async for message in websocket:
			print(f"Received: {message}")
			await websocket.send(f"Echo: {message}")  # Send response
	except websockets.exceptions.ConnectionClosed:
		print("Client disconnected")

async def main():
	server = await websockets.serve(handle_client, HOST, PORT)
	print(f"WebSocket server started on {HOST}:{PORT}")
	await server.wait_closed()

if __name__ == "__main__":
	asyncio.run(main())