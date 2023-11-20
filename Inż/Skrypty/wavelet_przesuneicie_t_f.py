import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import morlet

# Definiowanie parametrów
fs = 1000  # częstotliwość próbkowania
t = np.arange(0, 1, 1/fs)  # czas trwania sygnału: 1 sekunda

# Tworzenie sygnału - sumy trzech sinusoid
f1, f2, f3 = 5, 40, 90  # częstotliwości trzech sinusoid
signal = np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t) + np.sin(2*np.pi*f3*t)

# Funkcja falkowa Morleta
width = 7  # szerokość falki
morlet_wavelet = morlet(fs, w=width)
time_shift = -280  # przesunięcie w czasie (w próbkach)

# Zmiana skali funkcji falkowej Morleta
scaled_morlet_wavelet = 3 * morlet_wavelet / np.max(morlet_wavelet.real)
shifted_scaled_morlet_wavelet = np.roll(scaled_morlet_wavelet, time_shift)

# Parametr rozciągania/zwężania falki
stretch_factor = 3  # np. 0.5 oznacza zwężenie, 2 oznacza rozciągnięcie


# Zastosowanie rozciągania/zwężania do funkcji falkowej
if stretch_factor != 1:
    stretched_length = int(len(scaled_morlet_wavelet) * stretch_factor)
    stretched_morlet_wavelet = np.interp(np.linspace(0, 1, stretched_length), np.linspace(0, 1, len(scaled_morlet_wavelet)), scaled_morlet_wavelet.real)
    stretched_morlet_wavelet = np.roll(stretched_morlet_wavelet, int(time_shift * stretch_factor))

    # Przycięcie rozciągniętej falki do oryginalnej długości osi czasu
    if stretch_factor > 1:
        stretched_morlet_wavelet = stretched_morlet_wavelet[:len(t)]
else:
    stretched_morlet_wavelet = scaled_morlet_wavelet.real

# Tworzenie wykresu
plt.figure(figsize=(12, 6))
plt.plot(t, signal, label='Sygnał', alpha=0.5)
plt.plot(t, stretched_morlet_wavelet, label='Przesunięta i przeskalowana funkcja falkowa Morleta', alpha=1)
# ... [reszta kodu] ...

plt.xlabel('Czas [s]')
plt.ylabel('Amplituda')
plt.grid(True)

# Zapisywanie wykresu do pliku
plt.savefig('t_and_f_shift_morlet.png')
plt.show()
