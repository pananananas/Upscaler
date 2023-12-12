import matplotlib.pyplot as plt
from scipy.ndimage import zoom
import numpy as np

# Ustawienia początkowe
np.random.seed(0) # zapewnienie powtarzalności wyników
original_image = np.random.rand(4, 4) # przykładowy obraz 4x4 piksele
zoom_factor = 3 # czynnik powiększenia

# Interpolacja dwuliniowa przy użyciu funkcji 'zoom' z biblioteki scipy
interpolated_image = zoom(original_image, zoom_factor, order=1) # order=1 oznacza interpolację dwuliniową

# Funkcja do rysowania i zapisywania obrazu
def plot_and_save_image(image, grid_color, file_name):
    plt.figure(figsize=(6, 5))
    plt.imshow(image, cmap='gray', interpolation='nearest')

    plt.grid(True, which='both', color=grid_color, linestyle='-', linewidth=1)
    plt.xticks(np.arange(-0.5, image.shape[1], 1), minor=True)
    plt.yticks(np.arange(-0.5, image.shape[0], 1), minor=True)
    plt.grid(which="minor", color=grid_color, linestyle='-', linewidth=1)
    plt.savefig(file_name)

# Rysowanie i zapisywanie oryginalnego obrazu
plot_and_save_image(original_image, 'red', 'bilinear_original.png')

# Rysowanie i zapisywanie obrazu po interpolacji
plot_and_save_image(interpolated_image, 'blue', 'bilinear_enlarged.png')

# Ścieżki do zapisanych obrazów
original_image_path = 'bilinear_original.png'
interpolated_image_path = 'bilinear_enlarged.png'

original_image_path, interpolated_image_path
