import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import scipy.io.wavfile as wav
from scipy.signal import find_peaks
from os.path import dirname, join as pjoin
import time

pi = np.pi

data_dir = pjoin(dirname(__file__), 'gen')
wav_fname = pjoin(data_dir, "4.wav")
fs, _data = wav.read(wav_fname)
data = _data.flatten()

# BASIC CHARACTERS
ts = 1/fs  # Sampling period (ts)
N = len(data)  # Signal length in samples
l = N / fs  # Signal length in seconds
t = np.linspace(0, l, fs)  # Time Array
print(f"fs-{fs} N-{N} l={l}s")


# Fourier transformation
'''
(2/N)np.fft.fft() =>  (2/N)∑(x(t)exp(-jwht)) = (2/T)∫x(t)exp(-jwht)dt = Z[]

z[] => complex number array
Magnitude (Vm) = absolute of Z[]
Phase angle (p) = angle of Z[]
'''

f = fs * np.arange((N/2)) / N  # frequencies
Z = np.fft.fft(data)  # fourier transformation
Vm = np.abs(Z)  # Absolutes
ph = np.angle(Z)  # Phase angles
peaks, _ = find_peaks(Vm)  # Peak Points

# plotting
fig, ax = plt.subplots()
plt.plot(f, Vm)
plt.plot(peaks, Vm[peaks], "X")
plt.ylabel('Amplitude')
plt.xlabel('Frequency [Hz]')
plt.figure()
plt.show()

print(peaks)  # Frequencies
print(Vm[peaks])  # Amplitudes
print(ph[peaks])  # Phase ANgles

signal = 0*np.cos(2*pi*t + 0)
for x in peaks:
    # Sinusoidal wave relevant to peak
    s0 = Vm[x]*np.cos(2*pi*x*t + ph[x])
    plt.plot(t[:1000], s0[:1000])
    signal = signal + s0
plt.figure()

# play original sound
sd.play(data, fs)
time.sleep(1)

# play generated sound
sd.play(signal, fs)

plt.plot(t[:1000], data[:1000])
plt.figure()
plt.plot(t[:1000], signal[:1000], color="g")
plt.show()
