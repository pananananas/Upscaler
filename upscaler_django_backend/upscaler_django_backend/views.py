from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Image
from django.http import JsonResponse


@csrf_exempt
def upload_image(request):
    try:
        
        form = Image(image=request.FILES['image'])
        form.save()

#         # Tutaj możesz przetwarzać obraz za pomocą Pythona


        return JsonResponse({'message': 'Image uploaded successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)