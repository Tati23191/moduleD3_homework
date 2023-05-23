from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator


# Создаём модель товара
class News(models.Model):
    header = models.CharField(
        max_length=50,
        unique=True,
    )
    creationTime = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f'{self.header.title()}: {self.description[:50]}'