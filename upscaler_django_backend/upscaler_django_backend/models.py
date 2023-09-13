from django.db import models

class Image(models.Model):
    # Twoje pola modelu tutaj
    image = models.ImageField(upload_to='images/')
    class Meta:
        app_label = 'upscaler_django_backend'