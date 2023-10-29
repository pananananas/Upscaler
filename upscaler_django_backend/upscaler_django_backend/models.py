from django.db import models
import json

class Image(models.Model):

    image = models.ImageField(upload_to='images/')

    bilinear_image = models.ImageField(upload_to='upscaled_images/bilinear/', null=True, blank=True)
    dwsr_image = models.ImageField(upload_to='upscaled_images/dwsr/', null=True, blank=True)
    esrgan_image = models.ImageField(upload_to='upscaled_images/esrgan/', null=True, blank=True)
    
    original_height = models.PositiveIntegerField(null=True, blank=True)
    original_width = models.PositiveIntegerField(null=True, blank=True)
    dominant_colors = models.TextField(null=True, blank=True)  # This will store the JSON string of dominant colors


    def __str__(self):
        return f"Image {self.id}"  # String representation for the admin site and any time you use print on an instance of your model.
    
    def set_dominant_colors(self, colors_list):
        self.dominant_colors = json.dumps(colors_list)
        
    def get_dominant_colors(self):
        return json.loads(self.dominant_colors) if self.dominant_colors else None

    class Meta:
        app_label = 'upscaler_django_backend'