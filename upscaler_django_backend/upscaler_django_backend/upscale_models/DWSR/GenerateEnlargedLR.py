import os
import cv2
import numpy as np
from PIL import Image
from glob import glob

def generate_enlarged_lr(input_dir, output_dir, scale=2):
    """
    Generate enlarged Low Resolution images.

    Parameters:
        input_dir (str): Path to the directory containing input images.
        output_dir (str): Path to the directory where output images will be saved.
        scale (int): Scaling factor for enlarging images. Default is 2.
    """
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f'Start to generate enlarged LR training data SCALE {scale}')
    print(f'LR data from {input_dir}')
    print(f'Enlarged LR luminance store to {output_dir}')

    bicFileName = os.path.basename(input_dir)

    
    # Read the image
    BIC_img = cv2.imread(input_dir)
    
    # Resize the image
    BICBIC_img = cv2.resize(BIC_img, (BIC_img.shape[1]*scale, BIC_img.shape[0]*scale), interpolation=cv2.INTER_CUBIC)
    
    # Convert the image from BGR to YCrCb color space
    BICBIC_img_ycbcr = cv2.cvtColor(BICBIC_img, cv2.COLOR_BGR2YCrCb)
    
    # Extract the Y (luminance) channel and normalize it
    BICBIC_img_lum = BICBIC_img_ycbcr[:,:,0].astype(np.float32) / 255.0
    
    # Save the luminance image
    lum_image_path = os.path.join(output_dir, bicFileName)
    lum_image = Image.fromarray(np.uint8(BICBIC_img_lum * 255))
    lum_image.save(lum_image_path)


# generate_enlarged_lr("/Users/erykwojcik/Documents/GitHub/Upscaler/upscaler_django_backend/images/comic.png", "/Users/erykwojcik/Documents/GitHub/Upscaler/upscaler_django_backend/images/comic_enlarged_lr")