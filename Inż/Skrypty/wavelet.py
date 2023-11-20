import numpy as np
import pywt
import matplotlib.pyplot as plt

# Generating a more complex signal
t = np.linspace(0, 1, 1000, endpoint=False)
# Combining multiple sine waves
signal = np.sin(2 * np.pi * 5 * t) + np.sin(2 * np.pi * 10 * t) + np.sin(2 * np.pi * 20 * t)

# Adding noise
noise = np.random.normal(0, 0.5, signal.shape)
signal += noise

# Performing Continuous Wavelet Transform
scales = np.arange(1, 128)
coefficients, frequencies = pywt.cwt(signal, scales, 'cmor')

# Calculate the magnitude of the coefficients
coefficients_magnitude = np.abs(coefficients)

# Preparing data for LaTeX (time, scale, magnitude)
n = 100
X, Y = np.meshgrid(t[::n], scales)
data_for_latex = np.column_stack((X.ravel(), Y.ravel(), np.abs(coefficients[:, ::n]).ravel()))

# Saving the data for LaTeX
np.savetxt('Inż/Rozdziały/02.Podstawy_teoretyczne/wavelet_coefficients_magnitude.txt', data_for_latex)

# Optional: Visualizing the wavelet transform
plt.imshow(coefficients_magnitude, extent=[0, 1, 1, 128], cmap='PRGn', aspect='auto',
           vmax=coefficients_magnitude.max(), vmin=coefficients_magnitude.min())
plt.title("Wavelet Transform of a Complex Signal with Noise")
plt.xlabel("Time")
plt.ylabel("Scale")
plt.colorbar(label="Magnitude")
plt.show()

# Saving the magnitudes for LaTeX
# np.savetxt('Inż/Rozdziały/02.Podstawy_teoretyczne/wavelet_coefficients_magnitude.txt', coefficients_magnitude)





# np.savetxt('Inż/Rozdziały/02.Podstawy_teoretyczne/wavelet_coefficients.txt', coefficients)
# import pywt
# import matplotlib.pyplot as plt
# import numpy as np
# from PIL import Image

# def wavelet_transform(image_path, wavelet='haar'):
#     # Wczytanie obrazu
#     image = Image.open(image_path)
#     image = image.convert('L')  # Konwersja do skali szarości
#     data = np.array(image)

#     # Wykonanie transformacji falkowej
#     coeffs = pywt.dwt2(data, wavelet)
#     cA, (cH, cV, cD) = coeffs

#     # Zapisanie wyników jako obrazy
#     plt.imsave('approximation.png', cA, cmap='gray')
#     plt.imsave('horizontal_detail.png', cH, cmap='gray')
#     plt.imsave('vertical_detail.png', cV, cmap='gray')
#     plt.imsave('diagonal_detail.png', cD, cmap='gray')

#     # Rysowanie wyników
#     fig, axs = plt.subplots(2, 2, figsize=(12, 12))

#     axs[0, 0].imshow(cA, cmap='gray')
#     axs[0, 0].set_title('Approximation'), axs[0, 0].axis('off')

#     axs[0, 1].imshow(cH, cmap='gray')
#     axs[0, 1].set_title('Horizontal detail'), axs[0, 1].axis('off')

#     axs[1, 0].imshow(cV, cmap='gray')
#     axs[1, 0].set_title('Vertical detail'), axs[1, 0].axis('off')

#     axs[1, 1].imshow(cD, cmap='gray')
#     axs[1, 1].set_title('Diagonal detail'), axs[1, 1].axis('off')

#     plt.show()



# def plot_specific_wavelet(wavelet_type, scale, location):
#     # Define the time vector
#     t = np.linspace(-5, 5, 1000)

#     # Create a wavelet of the specified type
#     wavelet = pywt.ContinuousWavelet(wavelet_type)

#     # Compute the wavelet
#     psi, _ = wavelet.wavefun(length=len(t))

#     # Adjust the wavelet according to the scale and location
#     scaled_psi = scale * psi
#     shifted_psi = np.roll(scaled_psi, int(location * len(t)))

#     # Plot the wavelet
#     plt.figure()
#     plt.plot(t, shifted_psi.real, label='Real part')
#     # if np.iscomplexobj(shifted_psi):
#     #     plt.plot(t, shifted_psi.imag, label='Imaginary part', linestyle='--')
#     plt.xlabel('Time')
#     plt.ylabel('Amplitude')
#     # plt.title(f'{wavelet_type} Wavelet')
#     plt.legend()
#     plt.grid(True)

#     # Save the plot as an image
#     file_name = f'wavelet_{wavelet_type}.png'
#     plt.savefig(file_name, bbox_inches='tight', pad_inches=0)
#     plt.close()

#     return file_name



# def plot_sine_wave(start, end):
#     # Define the time vector within the specified range
#     t = np.linspace(start, end, 1000)

#     # Compute the sine wave
#     sine_wave = np.sin(t)

#     # Plot the sine wave
#     plt.figure()
#     plt.plot(t, sine_wave)
#     plt.xlabel('Time')
#     plt.ylabel('Amplitude')
#     plt.grid(True)

#     # Save the plot as an image
#     plt.savefig('sine_wave.png', bbox_inches='tight', pad_inches=0)
#     plt.close()

#     return 'sine_wave.png'


# def plot_discrete_wavelet(wavelet_type, scale, location):
#     # Create a wavelet of the specified type
#     wavelet = pywt.Wavelet(wavelet_type)

#     # Generate the wavelet function
#     length = int(2 ** np.ceil(np.log2(10 * scale)))
#     wavelet_function = pywt.waverec([np.ones((length,))], wavelet)

#     # Adjust the wavelet according to the scale and location
#     scaled_wavelet = scale * wavelet_function
#     shifted_wavelet = np.roll(scaled_wavelet, int(location * len(wavelet_function)))

#     # Create the time vector for plotting
#     t = np.linspace(-5, 5, len(shifted_wavelet))

#     # Plot the wavelet
#     plt.figure()
#     plt.plot(t, shifted_wavelet)
#     plt.xlabel('Time')
#     plt.ylabel('Amplitude')
#     plt.title(f'{wavelet_type} Wavelet')
#     plt.grid(True)

#     # Save the plot as an image
#     file_name = f'{wavelet_type}_wavelet.png'
#     plt.savefig(file_name, bbox_inches='tight', pad_inches=0)
#     plt.close()

#     return file_name

# # Plot Haar and Symlet wavelets





# # Example usage
# start = 0  # Start of the interval
# end = 12 * np.pi  # End of the interval
# # plot_sine_wave(start, end)




# # scale = 1.5 
# # location = 1
# # plot_morlet_wavelet(scale, location)

# wavelet_types = ['cmor1.5-1.0', 'gaus1', 'mexh', 'shan1.5-1.0']
# scale = 1.5  # Example scale
# location = 1  # Example location
# haar_image = plot_discrete_wavelet('haar', scale, location)
# sym5_image = plot_discrete_wavelet('sym5', scale, location)

# wavelet_images = [plot_specific_wavelet(wavelet, scale, location) for wavelet in wavelet_types]


# # wavelet_transform('Inż/Scripts/comic_DWSR_x4.png')
