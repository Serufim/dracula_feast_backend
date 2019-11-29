from django.db import models


# Create your models here.
class GameRole(models.Model):
    name = models.CharField(max_length=255)
    descriptions = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return f"{self.name}"
