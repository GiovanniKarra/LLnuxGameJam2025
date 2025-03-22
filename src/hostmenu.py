from ascengine.core import *
from freq import GameInstance
from game import Game
from player import Player
from utils import get_username


class HostMenu(GameObject):
	def __init__(self):
		me = Player()
		me.set_name(get_username())
		me.set_id(1)
		me.set_sprite(Sprite("###\n###\n###"))
		self.players = [me]
		self.player_list = GameObject(sprite=Sprite("\n".join([player.name for player in self.players])))
		super().__init__()

	def update(self):
		super().update()
		if self.tickcount < 5: return
		if Input.keypressed(Key.enter): self.start_game()
		self.player_list.set_sprite(Sprite("\n".join([player.name for player in self.players])))

	def start_game(self):
		Game(GameInstance(self.players))
		self.destroy()

	def destroy(self):
		self.player_list.destroy()
		return super().destroy()