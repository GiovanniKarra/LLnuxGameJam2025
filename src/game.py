from server import asyncio, main
from ascengine.core import *
from freq import GameInstance, get_input_freq


id_to_color = {
	1: "RED",
	2: "BLUE",
}

class Game(GameObject):
	def __init__(self, game_instance: GameInstance):
		self.game_instance = game_instance
		self.pointer = GameObject(sprite=Sprite("{BLUE;BOLD}^"))

		width, height = Display.get_size()
		self.player1 = GameObject(3, 3, sprite=game_instance.players[0].sprite)
		bar1 = GameObject()
		try: 
			self.player2 = GameObject(width-6, 3, sprite=game_instance.players[1].sprite)
			bar2 = GameObject()
		except:
			self.player2 = None
			bar2 = None
		self.bars = [bar1, bar2]
		scale_precision = 10
		min_freq, max_freq = game_instance.freq_range
		step = (max_freq-min_freq+1)//(scale_precision-1)
		scale_string = (" "*7).join([str(int(val))
							   for val in range(min_freq, max_freq+1, step)])
		self.scale = GameObject(15, 17, Sprite(scale_string))
		self.game_instance.reset()

		super().__init__()

	def update(self):
		self.game_instance.update(1/30)
		for i, player in enumerate(self.game_instance.players):
			min_freq, max_freq = self.game_instance.freq_range
			player.freq = get_input_freq()
			freq = player.freq
			time = self.game_instance.timers[i]
			max_time = self.game_instance.max_time
			bar_string = "\n".join(["{%s}#"%id_to_color[player.id]
						   for _ in range(int(7*time/max_time)+1)])
			self.bars[i].set_sprite(Sprite(bar_string))
			self.bars[i].set_position(15+int(min(max(freq-min_freq, 0)/(max_freq-min_freq), 1)*93), 15-int(7*time/max_time))
		self.pointer.set_position(15+int(min(max(self.game_instance.target-min_freq, 0)/(max_freq-min_freq), 1)*93), 16)
		super().update()