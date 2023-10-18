import os
import threading
from upscaler_django_backend.upscale_models.DWSR.GenerateEnlargedLR import generate_enlarged_lr  
from upscaler_django_backend.upscale_models.DWSR.DWSRx2 import process_image
from upscaler_django_backend.upscale_models.DWSR.FinalColorSR import generate_color_sr

def run_dwsr(input_image_path, scale):
    # Define paths
    enlarged_lr_dir = 'images/enlargedLR'
    sr_lum_dir = 'images/greyscaleSR'
    output_dir = 'images/output'
    fileName = os.path.basename(input_image_path)

    # Ensure directories exist
    for dir_path in [enlarged_lr_dir, sr_lum_dir, output_dir]:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)


    # 1. Generate enlarged LR images
    generate_enlarged_lr(input_image_path, enlarged_lr_dir, scale) 

    # 2. Process image with DWSR
    for image_filename in os.listdir(enlarged_lr_dir):
        input_path = os.path.join(enlarged_lr_dir, image_filename)
        process_image(input_path, sr_lum_dir)

    # 3. Generate color SR
    generate_color_sr(input_image_path, sr_lum_dir, output_dir, scale) 



    # TODO: Umieść obraz finalny w bazie danych, wyślij go na front