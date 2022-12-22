from os.path import dirname, join as pjoin
import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt


data_dir = pjoin(dirname(__file__), 'gen')
wav_fname = pjoin(data_dir, "4.wav")
fs, data1 = wav.read(wav_fname)
data = data1.flatten()

# BASIC CHARACTERS
ts = 1/fs  # Sampling period (ts)
N = len(data)  # Signal length in samples
l = N / fs  # Signal length in seconds
t = np.linspace(0, l, fs)  # Time Array


plt.plot(t[:5000], data[:5000])
plt.figtext(.2, .9, f"fs-{fs} N-{N} l={l}s")
plt.ylabel('Amplitude')
plt.xlabel('Time [s]')
plt.show()
