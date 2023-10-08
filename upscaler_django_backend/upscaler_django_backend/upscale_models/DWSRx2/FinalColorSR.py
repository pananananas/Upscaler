import cv2
import os
import glob

def generate_color_sr(input_dir, lum_dir, output_dir, scale=2):
    """
    Generate color Super-Resolution images.

    Parameters:
        input_dir (str): Path to the directory containing input bicubic downscaled images.
        lum_dir (str): Path to the directory containing super-resolved luminance images.
        output_dir (str): Path to the directory where output images will be saved.
        scale (int): Scaling factor for super-resolution. Default is 2.
    """
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Get the list of all files in the input directory
    input_images = glob.glob(os.path.join(input_dir, '*.png'))

    BICTESTDATA_bud = glob.glob(os.path.join(BICTESTDATA_PATH, '*.png'))

    print(f'Start to generate color SR SCALE {scale}')
    print(f'Luminance SR from {lum_dir}')
    print(f'Cb Cr channel from {input_dir}')
    print(f'Final color SR store to {output_dir}')


    bic_test_file_name = os.path.basename(input_dir)

    
    # Read bicubic down-scaled image
    bic_test_img = cv2.imread(lum_dir)
    
    # Upscale the bicubic down-scaled image
    bic_bic_test_img = cv2.resize(bic_test_img, (bic_test_img.shape[1]*scale, bic_test_img.shape[0]*scale), interpolation=cv2.INTER_CUBIC)
    
    # Convert to YCrCb color space
    test_img_ycbcr = cv2.cvtColor(bic_bic_test_img, cv2.COLOR_BGR2YCrCb)
    
    # Set the Y channel to zero
    test_img_ycbcr[:,:,0] = 0
    
    # Read the super-resolved luminance image
    sr_img = cv2.imread(os.path.join(lum_dir, bic_test_file_name), cv2.IMREAD_GRAYSCALE)
    
    # Replace the Y channel with the super-resolved image
    test_img_ycbcr[:,:,0] = sr_img
    
    # Convert back to BGR color space
    sr_color = cv2.cvtColor(test_img_ycbcr, cv2.COLOR_YCrCb2BGR)
    
    # Write the final super-resolved color image
    cv2.imwrite(os.path.join(output_dir, bic_test_file_name), sr_color)



input_image_path = '/images/comic.png'
sr_lum_dir = '/images/greyscaleSR/comic.png'
output_dir = '/images/output'

fileName = os.path.basename(input_image_path)

generate_color_sr(input_image_path, sr_lum_dir, output_dir, scale=2) 