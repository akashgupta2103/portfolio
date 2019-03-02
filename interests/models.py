from django.db import models

# Create your models here.
class Interest(models.Model):
    interestdetail = models.TextField(max_length=5000)