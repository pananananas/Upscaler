from django.db import models

class Image(models.Model):
    # Your original field
    image = models.ImageField(upload_to='images/')

    # New fields for upscaled images
    bilinear_image = models.ImageField(upload_to='upscaled_images/bilinear/', null=True, blank=True)  # for the Bilinear upscaled image
    dwsr_image = models.ImageField(upload_to='upscaled_images/dwsr/', null=True, blank=True)  # for the DWSR upscaled image
    esrgan_image = models.ImageField(upload_to='upscaled_images/esrgan/', null=True, blank=True)  # for the ESRGAN upscaled image
    
    
    class Meta:
        app_label = 'upscaler_django_backend'

    def __str__(self):
        return f"Image {self.id}"  # String representation for the admin site and any time you use print on an instance of your model.
