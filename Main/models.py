from django.db import models

# Create your models here.
class UpImg(models.Model):
    img = models.ImageField(upload_to = '/upload')
