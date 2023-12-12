import pywt
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def normalize_and_convert(array):
    """
    Normalize the array to [0, 255] and convert to uint8
    """
    array -= array.min()  # Shift the values to be >= 0
    array /= array.max()  # Scale the values to be <= 1
    array *= 255  # Scale the values to be in [0, 255]
    return array.astype(np.uint8)


def wavelet_decomposition(image_path, wavelet='haar', level=1):
    """
    Perform wavelet decomposition on an image and plot the results.

    :param image_path: Path to the input image.
    :param wavelet: Type of wavelet to use for decomposition.
    :param level: Level of decomposition.
    """
    # Load image
    image = Image.open(image_path).convert('L')  # convert image to grayscale
    image_data = np.array(image)

    # Perform wavelet decomposition
    coeffs = pywt.wavedec2(image_data, wavelet, level=level)

    # Save each sub-band
    Image.fromarray(normalize_and_convert(coeffs[0])).save(f'level_1_decomposition_LL.png')  # LL sub-band
    Image.fromarray(normalize_and_convert(coeffs[1][0])).save(f'level_1_decomposition_LH.png')  # LH sub-band
    Image.fromarray(normalize_and_convert(coeffs[1][1])).save(f'level_1_decomposition_HL.png')  # HL sub-band
    Image.fromarray(normalize_and_convert(coeffs[1][2])).save(f'level_1_decomposition_HH.png')  # HH sub-band

    print("Images saved successfully.")

    # Prepare plot
    fig, axes = plt.subplots(2, 2, figsize=(8, 8))
    titles = ['LL', 'LH', 'HL', 'HH ']

    # Plot each sub-band
    for i, ax in enumerate(axes.flat):
        if i == 0:
            # LL sub-band
            ax.imshow(coeffs[0], cmap=plt.cm.gray)
        else:
            # LH, HL, HH sub-bands
            ax.imshow(coeffs[1][i-1], cmap=plt.cm.gray)
        ax.set_title(titles[i], fontsize=10)
        ax.axis('off')

    plt.tight_layout()
    plt.show()

# Example usage
wavelet_decomposition('Inż/Skrypty/comic_DWSR_x4.png')
