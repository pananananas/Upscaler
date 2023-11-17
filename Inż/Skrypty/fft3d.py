import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Ustawienia
fs = 1000  # Częstotliwość próbkowania
t = np.linspace(0, 1, fs, endpoint=False)  # Wektor czasu
frequencies = [60, 120, 240, 480]  # Lista częstotliwości do generowania sygnałów
signals = [np.sin(2 * np.pi * f * t) for f in frequencies]  # Lista sygnałów
fft_results = [np.fft.fft(signal) for signal in signals]  # FFT każdego sygnału
fft_freqs = np.fft.fftfreq(t.size, 1/fs)  # Częstotliwości dla wyników FFT

# Utworzenie figury i osi 3D
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Wizualizacja sygnałów w dziedzinie czasu i ich FFT
for idx, (signal, fft_result) in enumerate(zip(signals, fft_results)):
    # Rysowanie sygnału w dziedzinie czasu
    ax.plot(t, signal, zs=idx, zdir='y', label=f'Signal {idx+1}')

    # Rysowanie magnitudy FFT w dziedzinie częstotliwości
    # Biorąc tylko połowę wyników, ponieważ druga połowa jest symetryczna
    fft_magnitude = np.abs(fft_result[:t.size // 2])
    freqs = fft_freqs[:t.size // 2]
    ax.plot(freqs, fft_magnitude, zs=idx, zdir='y', color='r')

# Etykiety osi
ax.set_xlabel('Czas [s]')
ax.set_ylabel('Indeks sygnału / częstotliwość [Hz]')
ax.set_zlabel('Amplituda')

# Ustawienie legendy
ax.legend()

# Ustawienie kąta widzenia
ax.view_init(elev=30, azim=70)

# Pokazanie wykresu
plt.show()
