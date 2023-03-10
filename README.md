# Signal Analysis

Signal generation combining sinusoidal waves and signal analysis using fourier transform

## Signal Generator

Simple signal produced by

signal = amplitude _ cos( 2pi _ frequency _ time_array _ phase_angle )

### Signal Generator Function

`Vm = amplitude
f = frequency
p = phase angle`

```python
def signalGenerator(Vm, f, p):
    signal = Vm*np.cos(2*pi*f*t + p)
    return signal
```

### generated signals

```python
# Musical Notes
D = signalGenerator(1, 294, 0)  # D294
F = signalGenerator(1, 349, 0)  # F349
A = signalGenerator(1, 440, 0)  # A440
C = signalGenerator(1, 523, 0)  # C523
```

generated audio files 👇

[D](./notes/D.wav) | [F](./notes/F.wav) | [A](./notes/A.wav) | [C](./notes/C.wav)

```python
# Signal Generator
s1 = signalGenerator(0.5, 400, pi)
s2 = s1*signalGenerator(0.5, 420, 2*pi)
s3 = s2*signalGenerator(1, 440, 0)
s4 = s3*signalGenerator(1, 520, pi/2)

s5 = scipy.signal.square(2*pi*400*t+0)
Signal = s4*s5
```

generated audio files 👇

[Test Signal 1](./gen/1.wav) | [Test Signal 2](./gen/2.wav) | [Test Signal 3](./gen/3.wav) | [Test Signal 4](./gen/4.wav)
