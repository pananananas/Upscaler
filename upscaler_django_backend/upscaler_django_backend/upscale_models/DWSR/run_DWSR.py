from upscaler_django_backend.upscale_models.DWSR.GenerateEnlargedLR import generate_enlarged_lr  
from upscaler_django_backend.upscale_models.DWSR.FinalColorSR import generate_color_sr
from upscaler_django_backend.upscale_models.DWSR.DWSRx4 import process_image_x4
from upscaler_django_backend.upscale_models.DWSR.DWSRx2 import process_image
from django.core.files import File
import time
import os


def run_dwsr(input_image_path, scale, image_instance):
    # Define paths
    enlarged_lr_dir = 'images/enlargedLR'
    sr_lum_dir = 'images/greyscaleSR'
    output_dir = 'images/output'
    fileName = os.path.basename(input_image_path)

    # Ensure directories exist
    for dir_path in [enlarged_lr_dir, sr_lum_dir, output_dir]:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    start = time.time()

    # 1. Generate enlarged LR images
    generate_enlarged_lr(input_image_path, enlarged_lr_dir, scale) 

    # 2. Process image with DWSR
    for image_filename in os.listdir(enlarged_lr_dir):
        input_path = os.path.join(enlarged_lr_dir, image_filename)
        if scale == 2:
            process_image(input_path, sr_lum_dir)   
        elif scale == 4:
            process_image_x4(input_path, sr_lum_dir)

    # 3. Generate color SR
    final_img_path = generate_color_sr(input_image_path, sr_lum_dir, output_dir, scale) 

    end = time.time()
    image_instance.dwsr_time = end - start
    
    print(f'Final image path: {final_img_path}')

    # 4. Save image to database
    with open(final_img_path, 'rb') as file:
        django_file = File(file)
        image_instance.dwsr_image.save(os.path.basename(final_img_path), django_file, save=True)