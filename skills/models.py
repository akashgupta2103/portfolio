from django.db import models

# Create your models here.

class Skill(models.Model):
    skillname = models.CharField(max_length=20)
    skillrating = models.CharField(max_length=5)
    barwidth = models.CharField(max_length=3)
	
    def __str__(self):
        return self.skillname
