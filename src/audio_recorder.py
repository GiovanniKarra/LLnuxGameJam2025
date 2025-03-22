import pyaudio
import numpy as np

from ascengine.core import Prefs, log


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
TICKRATE = int(Prefs.get_param("tickrate"))
BUFFER_SIZE = RATE
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

def get_input_freq():
	freq_spectrum = np.abs(np.fft.fft(audio_buffer))
	freqs = np.fft.fftfreq(len(audio_buffer), d=1/RATE)
	freq_spectrum = freq_spectrum[:len(freq_spectrum)//2]
	freqs = freqs[:len(freqs)//2]
	# import matplotlib.pyplot as plt
	# print(freqs[np.argmax(freq_spectrum)])
	# plt.plot(freqs, freq_spectrum)
	# plt.show()
	return freqs[np.argmax(freq_spectrum)]