from django.db import models


# Create your models here.
class GameRole(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название персонажа')
    descriptions = models.TextField(verbose_name='Описание карты')
    rules_description = models.TextField(verbose_name='Описание как в правилах', null=True)
    image = models.ImageField(upload_to='images', verbose_name='Изображение карты')

    def __str__(self):
        return f"{self.name}"
