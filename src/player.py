from ascengine.core import Sprite


class Player:
	def __init__(self):
		self.freq = 0
		self.id = 0
		self.sprite = Sprite()
		self.name = ""
	
	def set_id(self, new_id):
		self.id = new_id

	def set_name(self, new_name):
		self.name = new_name

	def set_sprite(self, new_sprite):
		self.sprite = new_sprite

	def set_freq(self, new_freq):
		self.freq = new_freq