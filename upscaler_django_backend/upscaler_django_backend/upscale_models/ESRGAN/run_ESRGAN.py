from upscaler_django_backend.upscale_models.ESRGAN import RRDBNet_arch as arch
from django.core.files import File
import numpy as np
import torch
import cv2
import os


def initialize_esrgan_model():
    # Initialize the ESRGAN model 
    model_path = 'upscaler_django_backend/upscale_models/ESRGAN/models/RRDB_ESRGAN_x4.pth'
    device = torch.device('cpu')
    model = arch.RRDBNet(3, 3, 64, 23, gc=32)
    model.load_state_dict(torch.load(model_path), strict=True)
    model.eval()
    model = model.to(device)
    return model, device


def process_image_with_esrgan(model, device, input_image_path):
    # Read the uploaded image
    img = cv2.imread(input_image_path, cv2.IMREAD_COLOR)
    img = img * 1.0 / 255
    img = torch.from_numpy(np.transpose(img[:, :, [2, 1, 0]], (2, 0, 1))).float()
    img_LR = img.unsqueeze(0)
    img_LR = img_LR.to(device)

    # Process the image with ESRGAN
    with torch.no_grad():
        output = model(img_LR).data.squeeze().float().cpu().clamp_(0, 1).numpy()
    
    output = np.transpose(output[[2, 1, 0], :, :], (1, 2, 0))
    output = (output * 255.0).round()
    return output


def save_output_image(output, input_image_path, image_instance):
    # Save the output image to images/output
    base_name = os.path.splitext(os.path.basename(input_image_path))[0]
    image_format = os.path.splitext(os.path.basename(input_image_path))[1]

    output_image_path = os.path.join('images', 'output', f"{base_name}_ESRGANx4{image_format}")
    cv2.imwrite(output_image_path, output)
    
    with open(output_image_path, 'rb') as file:
        django_file = File(file)
        image_instance.esrgan_image.save(os.path.basename(output_image_path), django_file, save=True)


def run_esrgan(input_image_path, image_instance):
    model, device = initialize_esrgan_model()
    output = process_image_with_esrgan(model, device, input_image_path)
    save_output_image(output, input_image_path, image_instance)
