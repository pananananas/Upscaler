import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def fft_transform_and_save(image_path):
    # Wczytanie obrazu i konwersja do skali szarości
    image = Image.open(image_path).convert('L')
    data = np.array(image)

    # Wykonanie FFT
    fft_result = np.fft.fft2(data)
    fft_shifted = np.fft.fftshift(fft_result)

    # Obliczenie modułu i fazy
    magnitude = np.abs(fft_shifted)
    phase = np.angle(fft_shifted)

    # Logarytmiczna skala dla lepszej wizualizacji
    magnitude_log = np.log1p(magnitude)

    # Zapisanie modułu i fazy jako obrazów
    plt.imsave('fft_magnitude.png', magnitude_log, cmap='gray')
    plt.imsave('fft_phase.png', phase, cmap='gray')

# Przykładowe użycie:
fft_transform_and_save('Inż/Scripts/comic_DWSR_x4.png')
