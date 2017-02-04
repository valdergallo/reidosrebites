from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name