# encoding: utf-8
from django.db import models
from django.contrib.sitemaps import ping_google


class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    is_draft = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False):
        super().save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            # Bare 'except' because we could get a variety
            # of HTTP-related exceptions.
            pass
