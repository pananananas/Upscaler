import pywt
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def wavelet_transform(image_path, wavelet='haar'):
    # Wczytanie obrazu
    image = Image.open(image_path)
    image = image.convert('L')  # Konwersja do skali szarości
    data = np.array(image)

    # Wykonanie transformacji falkowej
    coeffs = pywt.dwt2(data, wavelet)
    cA, (cH, cV, cD) = coeffs

    # Zapisanie wyników jako obrazy
    plt.imsave('approximation.png', cA, cmap='gray')
    plt.imsave('horizontal_detail.png', cH, cmap='gray')
    plt.imsave('vertical_detail.png', cV, cmap='gray')
    plt.imsave('diagonal_detail.png', cD, cmap='gray')

    # Rysowanie wyników
    fig, axs = plt.subplots(2, 2, figsize=(12, 12))

    axs[0, 0].imshow(cA, cmap='gray')
    axs[0, 0].set_title('Approximation'), axs[0, 0].axis('off')

    axs[0, 1].imshow(cH, cmap='gray')
    axs[0, 1].set_title('Horizontal detail'), axs[0, 1].axis('off')

    axs[1, 0].imshow(cV, cmap='gray')
    axs[1, 0].set_title('Vertical detail'), axs[1, 0].axis('off')

    axs[1, 1].imshow(cD, cmap='gray')
    axs[1, 1].set_title('Diagonal detail'), axs[1, 1].axis('off')

    plt.show()

# Przykładowe użycie:
wavelet_transform('Inż/Scripts/comic_DWSR_x4.png')
