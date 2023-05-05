from django.db import models

# Create your models here.
class ImageModel(models.Model):
    # name = models.CharField(max_length=100, default=None)
    # url = models.CharField(max_length=250, default=None)
    img = models.ImageField(upload_to='images/', default=None)

    def __str__(self):
        return self.img