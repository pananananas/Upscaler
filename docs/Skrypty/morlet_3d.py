import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Constants
k = 1
omega_0 = 4

# Time range
t = np.linspace(-4, 4, 400)

# Wave function
Psi = k * np.exp(1j * omega_0 * t) * np.exp(-t**2 / 2)

# Real and Imaginary parts
Re_Psi = Psi.real
Im_Psi = Psi.imag

# Creating a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plotting
ax.plot3D(Re_Psi, Im_Psi, t, 'blue')

# Labels
ax.set_xlabel('Re($\Psi$)')
ax.set_ylabel('Im($\Psi$)')
ax.set_zlabel('Time (t)')

# Title
ax.set_title('3D Plot of $\Psi(t)=ke^{i\omega_0 t} \cdot e^{-t^2/2}$')

np.savetxt('Inż/Rozdziały/02.Podstawy_teoretyczne/wave_data.txt', np.column_stack((t, Re_Psi, Im_Psi)), header='Re_Psi, Im_Psi, Time')

plt.show()

