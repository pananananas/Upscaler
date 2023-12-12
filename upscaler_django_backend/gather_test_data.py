import os
import django
import pandas as pd

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'upscaler_django_backend.settings')
django.setup()

from upscaler_django_backend.models import Image


def gather_data():
    data = []


    for img in Image.objects.all():
        # Sprawdź, czy wszystkie wymagane wartości są dostępne
        if img.original_width is not None and img.original_height is not None and \
           img.bilinear_time is not None and img.dwsr_time is not None and img.esrgan_time is not None:
            resolution = img.original_width * img.original_height
            data.append({
                "resolution": resolution,
                "bilinear_time": img.bilinear_time,
                "dwsr_time": img.dwsr_time,
                "esrgan_time": img.esrgan_time
            })

    df = pd.DataFrame(data)
    return df


if __name__ == "__main__":
    df = gather_data()
    # sort data
    df = df.sort_values(by=['resolution'])
    df.to_csv('image_data.csv', index=False)
    print(df.head())  # Tylko do celów testowych, aby zobaczyć pierwsze kilka wierszy
