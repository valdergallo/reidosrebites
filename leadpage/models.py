from django.db import models
from django.contrib.sitemaps import ping_google


class Entry(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False):
        super().save(force_insert, force_update)
        try:
            ping_google()
        except Exception:
            # Bare 'except' because we could get a variety
            # of HTTP-related exceptions.
            pass
