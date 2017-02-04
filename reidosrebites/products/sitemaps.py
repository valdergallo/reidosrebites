# encoding: utf-8
from django.contrib.sitemaps import Sitemap
from .models import Product

class ProductsSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Product.objects.filter(is_draft=False)

    def lastmod(self, obj):
        return obj.pub_date
