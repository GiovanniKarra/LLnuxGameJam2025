import pyaudio
import numpy as np

# Audio settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100  # 44.1 kHz
CHUNK = 1024  # Buffer size
BUFFER_SIZE = RATE * 5  # 5 seconds of audio data
audio_buffer = np.zeros(BUFFER_SIZE, dtype=np.int16)  # Fixed-length buffer

def callback(in_data, frame_count, time_info, status):
    """Callback function to update the circular buffer."""
    global audio_buffer
    new_data = np.frombuffer(in_data, dtype=np.int16)
    
    # Shift buffer left and append new data
    audio_buffer = np.roll(audio_buffer, -len(new_data))
    audio_buffer[-len(new_data):] = new_data
    
    return (None, pyaudio.paContinue)

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open a non-blocking stream
stream = audio.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    stream_callback=callback)

stream.start_stream()

print("Recording... Press Ctrl+C to stop.")
try:
    while True:
        pass  # Keep the program running
except KeyboardInterrupt:
    print("\nStopping recording...")

# Stop and close the stream
stream.stop_stream()
stream.close()
audio.terminate()

print(f"Final buffer contains {len(audio_buffer)} samples.")

final_audio = np.frombuffer(audio_buffer, dtype=np.int16)

import matplotlib.pyplot as plt

plt.plot(np.linspace(0, 1, len(final_audio)), final_audio)
plt.show()

from scipy.fft import fft

freq_spectrum = np.abs(fft(final_audio))
print(freq_spectrum)
freqs = np.fft.fftfreq(len(final_audio), d=1/44100)  # Frequency axis
plt.plot(freqs[:len(freqs)//2], freq_spectrum[:len(freq_spectrum)//2])
plt.show()