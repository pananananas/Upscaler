from PIL import Image as PILImage
from sklearn.cluster import KMeans
from collections import Counter
import numpy as np
import cv2
import os

def clear_data_folders():
    # delete every item in folders:
    folder = [                              #  Oznaczone czyszczą baze danych jak sie odkomentuje
            #   'images',                     #
              'images/output', 
              'images/enlargedLR', 
              'images/greyscaleSR', 
            #   'upscaled_images',            #
            #   'upscaled_images/bilinear',   #
            #   'upscaled_images/dwsr',       #   
            #   'upscaled_images/esrgan'      #
              ]
    
    for f in folder:
        for file in os.listdir(f):
            file_path = os.path.join(f, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)


def clear_helper_folders():
    folder = ['images/enlargedLR', 
              'images/greyscaleSR']
    # delete folders:
    for f in folder:
        for file in os.listdir(f):
            file_path = os.path.join(f, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)


def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

def extract_image_info(input_image_path, image_instance):
    with PILImage.open(input_image_path) as img:
        # Set width and height
        image_instance.original_width = img.width
        image_instance.original_height = img.height
        image_instance.save()

        # Reshape the image data for k-means
        pixels = np.array(img.getdata())
        pixels = pixels.reshape(-1, 3)

        # Apply K-Means Clustering
        kmeans = KMeans(n_clusters=5)
        kmeans.fit(pixels)

        # Find Cluster Centers
        dominant_colors = kmeans.cluster_centers_

        # Convert dominant colors to a list of HEX strings
        dominant_colors_list = [rgb_to_hex(tuple(map(int, color))) for color in dominant_colors]
        image_instance.set_dominant_colors(dominant_colors_list)

        # Save the image instance
        image_instance.save()