import cv2
import os
import glob

def generate_color_sr(input_dir, lum_dir, output_dir, scale=2):

    # BICTESTDATA_bud = glob.glob(os.path.join(input_dir, '*.png'))

    # Print messages
    print(f'Start to generate color SR SCALE {scale}')
    print(f'Luminance SR from {lum_dir}')
    print(f'Cb Cr channel from {input_dir}')
    print(f'Finial color SR store to {output_dir}')

    # Loop through all images
    # for img_idx, bic_test_file_path in enumerate(BICTESTDATA_bud):
    bic_test_file_name = os.path.basename(input_dir)
    # print(f'Image: {img_idx + 1} | {bic_test_file_name}')
    
    # Read bicubic down-scaled image
    bic_test_img = cv2.imread(input_dir)
    
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
    
    # Add suffix to the file name
    bic_test_file_name = os.path.splitext(bic_test_file_name)[0] + '_DWSRx4.png'

    # Write the final super-resolved color image
    cv2.imwrite(os.path.join(output_dir, bic_test_file_name), sr_color)

    # Retun the final super-resolved color image
    return sr_color