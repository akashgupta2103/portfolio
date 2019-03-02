from django.db import models

# Create your models here.
class Education(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=300)
