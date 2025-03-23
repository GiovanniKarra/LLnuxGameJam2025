import numpy as np
from ascengine.core import *

from audio_recorder import get_audio_buffer
from mainmenu import MainMenu


if __name__ == "__main__":
	try:
		with open("username.txt", "r") as f:
			username = f.read()
	except:
		username = input("Enter your username: ")
		with open("username.txt", "w") as f:
			f.write(username)
	Prefs.set_param("width", 130)
	Prefs.set_param("height", 20)
	initialize_engine()

	MainMenu()

	main_loop()