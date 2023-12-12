import os
from PIL import Image

def downscale_images_in_folder(folder_path, scale_factor=16, postfix='_downscaled'):
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            img_path = os.path.join(folder_path, filename)
            with Image.open(img_path) as img:
                # Compute new dimensions
                new_width = img.width // scale_factor
                new_height = img.height // scale_factor

                # Resize the image
                img_resized = img.resize((new_width, new_height), Image.ANTIALIAS)

                # Create a new filename with the postfix
                name, ext = os.path.splitext(filename)
                new_filename = f"{name}{postfix}{ext}"
                new_img_path = os.path.join(folder_path, new_filename)

                # Save the resized image with the new filename
                img_resized.save(new_img_path)

# Path to the 'imgs' folder
folder_path = 'imgs'
downscale_images_in_folder(folder_path)
