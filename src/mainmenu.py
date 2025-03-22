from ascengine.core import *
from hostmenu import HostMenu


class MainMenu(GameObject):
	def __init__(self):
		width, height = Display.get_size()
		title_string = "Pilou Pilou"
		create_game_string = "Host game"
		join_game_string = "Join game"
		self.title = GameObject(x=(width//2-len(title_string)//2-1), sprite=Sprite("{BOLD;BLUE;UNDERLINE}%s"%title_string))
		self.create_game = GameObject(x=(width//2-len(title_string)//2), y=10, sprite=Sprite("%s"%create_game_string))
		self.join_game = GameObject(x=(width//2-len(title_string)//2), y=12, sprite=Sprite("%s"%join_game_string))

		self.pointer = GameObject(sprite=Sprite("{BLUE}>"))
		self.selected = 0
		super().__init__()
	
	def update(self):
		if Input.keypressed(Key.enter):
			HostMenu()
			self.destroy()
		self.selected += Input.keypressed(Key.down)
		self.selected -= Input.keypressed(Key.up)
		self.selected = self.selected%2
		if self.selected == 0:
			pointer_pos = (self.create_game.get_position()[0]-2, self.create_game.get_position()[1])
		elif self.selected == 1:
			pointer_pos = (self.join_game.get_position()[0]-2, self.join_game.get_position()[1])
		self.pointer.set_position(*pointer_pos)
		return super().update()
	
	def destroy(self):
		self.title.destroy()
		self.join_game.destroy()
		self.create_game.destroy()
		self.pointer.destroy()
		super().destroy()