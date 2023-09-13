from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Image

@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        form = Image(image=request.FILES['image'])
        form.save()

        # Tutaj możesz przetwarzać obraz za pomocą Pythona

        return JsonResponse({'message': 'Obraz został przesłany i przetworzony!'})

    return JsonResponse({'message': 'Niepoprawna metoda.'})