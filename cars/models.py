from django.db import models

# Create your models here.

class CarAd(models.Model):
    link = models.URLField()
    date = models.CharField(max_length=100)
    img = models.URLField()
    price = models.DecimalField(decimal_places=2, max_digits=7)
    model = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    comment = models.CharField(max_length=400)
    seller = models.CharField(max_length=100)

    def __str__(self):
        return self.model