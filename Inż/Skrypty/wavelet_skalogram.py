import numpy as np
import matplotlib.pyplot as plt
import pywt

# Parameters for the sinusoidal signal
frequency = 5  # frequency of the sinusoidal signal
sampling_rate = 100  # samples per second
t = np.arange(0, 1, 1/sampling_rate)  # time vector

# Generating a sinusoidal signal
sinus_signal = np.sin(2 * np.pi * frequency * t)

# Perform Continuous Wavelet Transform (CWT)
scales = np.arange(1, 128)
cwtmatr, freqs = pywt.cwt(sinus_signal, scales, 'cmor')

# Adjusting the layout to move the colorbar
plt.figure(figsize=(12, 8))
gs = plt.GridSpec(2, 2, width_ratios=[30, 1])

# Plotting the sinusoidal signal
ax1 = plt.subplot(gs[0, 0])
plt.plot(t, sinus_signal)
# plt.title('Sinusoidal Signal')

plt.ylabel('Amplituda')

# Plotting the wavelet transform (scalogram)
ax2 = plt.subplot(gs[1, 0])
cax = plt.imshow(abs(cwtmatr), extent=[0, 1, 1, 128], cmap='PRGn', aspect='auto',
                 vmax=abs(cwtmatr).max(), vmin=-abs(cwtmatr).max())
# plt.title('Scalogram')
plt.ylabel('Częstotliwość')
plt.xlabel('Czas')

# Adding the colorbar
plt.colorbar(cax, cax=plt.subplot(gs[:, 1]))

plt.tight_layout()
plt.show()
