from ascengine.core import *
import numpy as np
from audio_recorder import get_audio_buffer

def get_username():
	with open("username.txt", "r") as f:
		username = f.read()
	return username


class AudioDisplay(GameObject):
	def update(self):
		buffer = get_audio_buffer()
		N = len(buffer)
		width, height = Display.get_size()
		sprite_matrix = [[" " for _ in range(width)] for _ in range(height)]
		for i in range(width):
			start_index = N//width*i
			end_index = min(N//width*(i+1), N)
			val = np.mean(buffer[start_index:end_index])/100
			val = int(np.clip(val, -height//2, height//2-1))
			sprite_matrix[val+height//2][i] = "{38;2;255;%d;%d}#"%(256-int(np.abs(2*val/height)*255+1), 256-int(np.abs(2*val/height)*255+1))
		self.set_sprite(Sprite("\n".join(["".join(line) for line in sprite_matrix])))
		super().update()