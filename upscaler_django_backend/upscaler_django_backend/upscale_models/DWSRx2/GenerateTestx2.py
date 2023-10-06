import cv2
import os
import numpy as np
from PIL import Image
from glob import glob

# For NTIRE 2017 Super-Resolution Challenge
# Track 1: Bicubic downscaling - x2
# To produce enlarged LR testing data

SCALE = 2
BICDATA_PATH = f'./Testx{SCALE}Color/'
STORDATA_PATH = f'./Testx{SCALE}Lum'

# Ensure output directory exists
if not os.path.exists(STORDATA_PATH):
    os.makedirs(STORDATA_PATH)

# Get all .png files in BICDATA_PATH
BICDATA_bud = glob(os.path.join(BICDATA_PATH, '*.png'))

print(f'Start to generate enlarged LR training data SCALE {SCALE}')
print(f'LR data from {BICDATA_PATH}')
print(f'Enlarged LR luminance store to {STORDATA_PATH}')

for img_idx, bic_file_path in enumerate(BICDATA_bud):
    bicFileName = os.path.basename(bic_file_path)
    print(f'   Idx {img_idx+1}: {bicFileName}')
    
    # Read the image
    BIC_img = cv2.imread(bic_file_path)
    
    # Resize the image
    BICBIC_img = cv2.resize(BIC_img, (BIC_img.shape[1]*SCALE, BIC_img.shape[0]*SCALE), interpolation=cv2.INTER_CUBIC)
    
    # Convert the image from BGR to YCrCb color space
    BICBIC_img_ycbcr = cv2.cvtColor(BICBIC_img, cv2.COLOR_BGR2YCrCb)
    
    # Extract the Y (luminance) channel and normalize it
    BICBIC_img_lum = BICBIC_img_ycbcr[:,:,0].astype(np.float32) / 255.0
    
    # Save the luminance image
    lum_image_path = os.path.join(STORDATA_PATH, bicFileName)
    lum_image = Image.fromarray(np.uint8(BICBIC_img_lum * 255))
    lum_image.save(lum_image_path)
