import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import sounddevice as sd
import scipy.signal
pi = np.pi

# FS - Sample frequency of the generated signal
fs = 44100
# t - Time Array
t = np.linspace(0, 1, fs)

'''
Simple signal produced by
signal = amplitude*cos(2pi*frequency*time_array + phase_angle)
'''
signal = 0.5*np.cos(2*pi*400*t + 0)


sd.play(signal, fs)
wav.write("audio.wav", fs, signal)
plt.plot(t[:2000], (signal)[:2000])
plt.ylabel('Amplitude')
plt.xlabel('Time [s]')
plt.show()
