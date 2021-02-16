from django.db import models

# Create your models here.

class engryimg (models.Model):
    image = models.ImageField(upload_to='userimage/')

    def __str__(self):
        return self.image

