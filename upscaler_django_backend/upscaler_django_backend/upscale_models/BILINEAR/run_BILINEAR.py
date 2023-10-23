import cv2
import os


def run_bilinear(input_image_path, scale):
    # Read the uploaded image file
    img = cv2.imread(input_image_path, cv2.IMREAD_COLOR)
    
    # Calculate the new dimensions
    height, width = img.shape[:2]
    new_width, new_height = width * scale, height * scale

    # Resize the image using bilinear interpolation
    img_resized = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

    # Construct the output file path
    base_name = os.path.splitext(os.path.basename(input_image_path))[0]
    image_format = os.path.splitext(os.path.basename(input_image_path))[1]
    output_image_path = os.path.join('images', 'output', f"{base_name}_BILINEARx{scale}{image_format}")

    # Save the output image to the specified path
    cv2.imwrite(output_image_path, img_resized)
