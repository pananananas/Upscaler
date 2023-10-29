from PIL import Image as PILImage
from collections import Counter
import cv2
import os

def clear_data_folders():
    # delete every item in folders:
    folder = [                              # TODO: Usuń foldery z listy, eby obrazy zapisywały się w bazie danych
              'images',                     #
              'images/output', 
              'images/enlargedLR', 
              'images/greyscaleSR', 
              'upscaled_images',            #
              'upscaled_images/bilinear',   #
              'upscaled_images/dwsr',       #   
              'upscaled_images/esrgan'      #
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


def extract_image_info(input_image_path, image_instance):
    with PILImage.open(input_image_path) as img:
        # Set width and height
        image_instance.original_width = img.width
        image_instance.original_height = img.height

        # Extract and set dominant colors
        pixels = img.getdata()
        colors = Counter(pixels)
        dominant_colors = colors.most_common(5)  # Get top 5 dominant colors

        # Convert dominant colors to a list of RGB tuples
        dominant_colors_list = [color[0] for color in dominant_colors]
        image_instance.set_dominant_colors(dominant_colors_list)

        # Save the image instance
        image_instance.save()