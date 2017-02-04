from django.contrib.sitemaps import Sitemap
from .models import Entry
from django.urls import reverse


class LeadPageSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Entry.objects.filter(is_draft=False)

    def lastmod(self, obj):
        return obj.pub_date


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['main']

    def location(self, item):
        return reverse(item)
