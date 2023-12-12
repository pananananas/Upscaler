import numpy as np
import matplotlib.pyplot as plt
import pywt

# Define the constants for the Morlet wavelet function
omega = 5.0  # Frequency of the cosine
k0 = 1.0     # Scale factor for the wavelet

# Define the time vector
t = np.linspace(-5, 5, 1000)

# Define the Morlet wavelet function
morlet_wavelet = k0 * np.cos(omega * t) * np.exp(-t**2 / 2)

# Define the Gaussian envelope function
gaussian_envelope = np.exp(-t**2 / 2)

# Plot the Morlet wavelet function
plt.figure(figsize=(12, 4))
plt.plot(t, morlet_wavelet, label=r'$\Psi(t)=k_0 \cdot \cos(\omega t) \cdot e^{-t^2 / 2}$')

# Plot the Gaussian envelope function
plt.plot(t, gaussian_envelope, label=r'$e^{-t^2 / 2}$', linestyle='--')

plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

plt.show()

