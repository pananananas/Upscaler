import cv2
import numpy as np
import os
import glob

# Constants
SCALE = 2
# Other scale options:
# SCALE = 3
# SCALE = 4

# Paths
BICTESTDATA_PATH = f'./Testx{SCALE}Color/'
SRDATA_PATH = f'./Resultx{SCALE}Lum/'
STOR_PATH = f'./Resultx{SCALE}Color/'

# Get the list of all files in the directory
BICTESTDATA_bud = glob.glob(os.path.join(BICTESTDATA_PATH, '*.png'))

# Print messages
print(f'Start to generate color SR SCALE {SCALE}')
print(f'Luminance SR from {SRDATA_PATH}')
print(f'Cb Cr channel from {BICTESTDATA_PATH}')
print(f'Finial color SR store to {STOR_PATH}')

# Loop through all images
for img_idx, bic_test_file_path in enumerate(BICTESTDATA_bud):
    bic_test_file_name = os.path.basename(bic_test_file_path)
    print(f'Image: {img_idx + 1} | {bic_test_file_name}')
    
    # Read bicubic down-scaled image
    bic_test_img = cv2.imread(bic_test_file_path)
    
    # Upscale the bicubic down-scaled image
    bic_bic_test_img = cv2.resize(bic_test_img, (bic_test_img.shape[1]*SCALE, bic_test_img.shape[0]*SCALE), interpolation=cv2.INTER_CUBIC)
    
    # Convert to YCrCb color space
    test_img_ycbcr = cv2.cvtColor(bic_bic_test_img, cv2.COLOR_BGR2YCrCb)
    
    # Set the Y channel to zero
    test_img_ycbcr[:,:,0] = 0
    
    # Read the super-resolved luminance image
    sr_img = cv2.imread(os.path.join(SRDATA_PATH, bic_test_file_name), cv2.IMREAD_GRAYSCALE)
    
    # Replace the Y channel with the super-resolved image
    test_img_ycbcr[:,:,0] = sr_img
    
    # Convert back to BGR color space
    sr_color = cv2.cvtColor(test_img_ycbcr, cv2.COLOR_YCrCb2BGR)
    
    # Write the final super-resolved color image
    cv2.imwrite(os.path.join(STOR_PATH, bic_test_file_name), sr_color)
