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
'''
signalGenerator parameters
Vm = amplitude
f = frequency
p = phase angle
'''


def signalGenerator(Vm, f, p):
    signal = Vm*np.cos(2*pi*f*t + p)
    return signal


# Musical Notes
D = signalGenerator(1, 294, 0)  # D294
F = signalGenerator(1, 349, 0)  # F349
A = signalGenerator(1, 440, 0)  # A440
C = signalGenerator(1, 523, 0)  # C523


sd.play(C, fs)
wav.write("notes/C.wav", fs, C)
plt.plot(t[:2000], (C)[:2000])
plt.ylabel('Amplitude')
plt.xlabel('Time [s]')
plt.show()
