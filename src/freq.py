from time import sleep
from random import randint

from audio_recorder import get_input_freq
from player import Player


class GameInstance:
	def __init__(self, players, rounds=5, range=(220, 440)):
		self.players : list[Player] = players
		self.freq_range = range
		self.rounds = rounds
		self.timers = [0.0 for _ in players]
		self.scores = [0 for _ in players]
		self.target = 0
		self.max_time = 5

	def update(self, delta):
		for i, player in enumerate(self.players):
			freq = player.freq
			if abs(freq-self.target) < 10:
				self.timers[i] += delta
			else:
				self.timers[i] = 0
			if self.timers[i] >= self.max_time:
				self.new_round(i)
			# print(f"\rTarget frequency: {self.target}Hz\tYour frequency: {freq}Hz\tCorrect timer: {self.timers[i]}s", end="")
		return self.rounds <= 0

	def reset(self, rounds=5):
		self.rounds = rounds
		self.timers = [0.0 for _ in self.players]
		self.scores = [0 for _ in self.players]
		self.target = randint(*self.freq_range)
		self.max_time = 5

	def new_round(self, winner=None, score=0):
		if winner != None:
			self.scores[winner] += score
		self.target = randint(*self.freq_range)
		self.rounds -= 1
	