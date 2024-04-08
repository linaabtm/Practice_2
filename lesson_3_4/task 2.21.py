import numpy as np
import matplotlib.pyplot as plt

tmax = 1
dt = 0.0025
t = np.arange(0, tmax, dt)
freq = 10
wave = np.sin(2 * np.pi * freq * t) + np.sin(2 * np.pi * 2 * freq * t)
noise = 2 * (2 * np.random.sample(t.size) - 1)

signal = np.fft.fft(wave + noise, t.size)

freqs = np.fft.fftfreq(t.size, dt)

Spectrum = np.abs(signal) / t.size
L = np.arange(1, t.size // 2, dtype = int)

ind = Spectrum > 0.2
Spectrum_clean = Spectrum * ind

signal_clean = ind * signal
isignal = np.fft.ifft(signal_clean)

plt.plot(t, wave + noise, lw = 1, color = 'tab:blue', label = 'noisy')
plt.xlim(0, 0.5)
plt.plot(isignal, lw=2, color='tab:red')
plt.xlabel('time', fontsize=14)
plt.ylabel('amplitude', fontsize=14)
plt.show()

