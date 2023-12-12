import numpy as np
import cv2
from PIL import Image

def nearest_neighbor_zoom(image, zoom_factor=4):
    # Pobieranie rozmiarów oryginalnego obrazu
    original_height, original_width = image.shape[:2]

    # Obliczanie rozmiarów nowego obrazu
    new_height, new_width = original_height * zoom_factor, original_width * zoom_factor

    # Tworzenie nowego obrazu o powiększonych rozmiarach
    zoomed_image = np.zeros((new_height, new_width, image.shape[2]), dtype=image.dtype)

    # Przypisywanie wartości pikseli metodą najbliższego sąsiada
    for y in range(new_height):
        for x in range(new_width):
            # Najbliższy sąsiad z oryginalnego obrazu
            nearest_x = min(original_width - 1, int(x / zoom_factor))
            nearest_y = min(original_height - 1, int(y / zoom_factor))
            # Przypisanie wartości piksela
            zoomed_image[y, x] = image[nearest_y, nearest_x]

    return zoomed_image

# Wczytanie obrazu
input_image = cv2.imread('imgs/baboon.png')  # Podmień 'path_to_your_image.jpg' na ścieżkę do swojego obrazu

# Powiększenie obrazu
output_image = nearest_neighbor_zoom(input_image)

# Zapisanie powiększonego obrazu
cv2.imwrite('baboon_NN_x4.png', output_image)  # Podmień 'path_to_save_zoomed_image.jpg' na swoją ścieżkę
