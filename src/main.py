import numpy as np
from ascengine.core import *

from audio_recorder import get_audio_buffer


class AudioDisplay(GameObject):
	def update(self):
		buffer = get_audio_buffer()
		N = len(buffer)
		width, height = Display.get_size()
		sprite_matrix = [[" " for _ in range(width)] for _ in range(height)]
		for i in range(width):
			start_index = N//width*i
			end_index = min(N//width*(i+1), N)
			val = np.mean(buffer[start_index:end_index])/1000
			val = int(np.clip(val, -height//2, height//2-1))
			sprite_matrix[val+height//2][i] = "{38;2;255;%d;%d}#"%(256-int(np.abs(2*val/height)*255+1), 256-int(np.abs(2*val/height)*255+1))
		self.set_sprite(Sprite("\n".join(["".join(line) for line in sprite_matrix])))
		super().update()


if __name__ == "__main__":
	Prefs.set_param("width", 130)
	Prefs.set_param("height", 20)
	initialize_engine()

	AudioDisplay()
	main_loop()