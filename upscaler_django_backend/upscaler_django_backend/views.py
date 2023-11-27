from upscaler_django_backend.helper_methods.helper_methods import clear_data_folders
from upscaler_django_backend.helper_methods.helper_methods import extract_image_info
from upscaler_django_backend.upscale_models.BILINEAR.run_BILINEAR import run_bilinear
from upscaler_django_backend.upscale_models.ESRGAN.run_ESRGAN import run_esrgan
from upscaler_django_backend.upscale_models.DWSR.run_DWSR import run_dwsr
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Image
import threading



@csrf_exempt
def upload_image(request):
    try:
        clear_data_folders()
        
        form = Image(image=request.FILES['image'])
        form.save()

        input_image_path = form.image.path
        thread4 = threading.Thread(target=extract_image_info, args=(input_image_path, form))
        thread1 = threading.Thread(target=run_bilinear, args=(input_image_path, 4, form))
        thread2 = threading.Thread(target=run_dwsr, args=(input_image_path, 4, form))
        thread3 = threading.Thread(target=run_esrgan, args=(input_image_path, form))
        
        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()

        # thread1.join()
        # thread2.join()
        # thread3.join()
        
        image = Image.objects.latest('id')  # Gets the latest entry
        return JsonResponse({'message': 'Image uploaded and processing started', 'image_id': image.id})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
def get_image(request, image_id, image_type):
    try:
        image = get_object_or_404(Image, id=image_id)

        if image_type == 'bilinear':    
            image_url = image.bilinear_image.url
        elif image_type == 'dwsr':
            image_url = image.dwsr_image.url
        elif image_type == 'esrgan':
            image_url = image.esrgan_image.url
        else:
            image_url = image.image.url

        return JsonResponse({'image_url': image_url})
    
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def get_image_info(request, image_id):
    try:
        # Fetch the specific Image instance using the provided image_id
        image = get_object_or_404(Image, id=image_id)
        
        # Extract the width, height, and dominant colors from the Image instance
        width = image.original_width
        height = image.original_height

        dominant_colors = image.get_dominant_colors()
        
        # Return the extracted information in JSON format
        return JsonResponse({
            'width': width,
            'height': height,
            'colors': dominant_colors

        })
    except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
