from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Image
import os
import cv2
import numpy as np
import torch
import threading
from upscaler_django_backend.upscale_models.ESRGAN import RRDBNet_arch as arch

# Initialize the ESRGAN model (Better to do this once rather than for each request)
model_path = 'upscaler_django_backend/upscale_models/ESRGAN/models/RRDB_ESRGAN_x4.pth'
device = torch.device('cpu')

model = arch.RRDBNet(3, 3, 64, 23, gc=32)
model.load_state_dict(torch.load(model_path), strict=True)
model.eval()
model = model.to(device)

def run_esrgan(input_image_path):
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

    # Save the output image to images/output
    base_name = os.path.splitext(os.path.basename(input_image_path))[0]
    output_image_path = os.path.join('images', 'output', f"{base_name}_esrgan.png")
    cv2.imwrite(output_image_path, output)
    
    # For the sake of this example, the output_image_path is simply returned.
    # In a real-world scenario, you might want to send a notification to the user, store the result in a database, etc.
    return output_image_path

@csrf_exempt
def upload_image(request):
    try:
        form = Image(image=request.FILES['image'])
        form.save()

        # Get the path where the image was saved
        input_image_path = form.image.path

        # Run ESRGAN on another thread
        thread = threading.Thread(target=run_esrgan, args=(input_image_path,))
        thread.start()

        return JsonResponse({'message': 'Image uploaded and processing started'})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
