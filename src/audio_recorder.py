import pyaudio
import numpy as np

from ascengine.core import Prefs, log


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
TICKRATE = int(Prefs.get_param("tickrate"))
BUFFER_SIZE = RATE//TICKRATE
audio_buffer = np.zeros(BUFFER_SIZE, dtype=np.int16)

def callback(in_data, frame_count, time_info, status):
	new_data = np.frombuffer(in_data, dtype=np.int16)
	
	global audio_buffer
	audio_buffer = np.roll(audio_buffer, -len(new_data))
	audio_buffer[-len(new_data):] = new_data
	
	return None, pyaudio.paContinue

audio = pyaudio.PyAudio()

stream = audio.open(format=FORMAT,
					channels=CHANNELS,
					rate=RATE,
					input=True,
					frames_per_buffer=CHUNK,
					stream_callback=callback)

stream.start_stream()


def get_audio_buffer():
	return audio_buffer