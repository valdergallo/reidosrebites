# encoding: utf-8
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from leadpage.sitemaps import StaticViewSitemap
from leadpage.views import LeadPageView
from leadpage.sitemaps import LeadPageSitemap
from products.sitemaps import ProductsSitemap


sitemaps = {
    'static': StaticViewSitemap,
    'lead': LeadPageSitemap,
    'products': ProductsSitemap,
}

urlpatterns = [
    url(r'^$', LeadPageView.as_view(), name='main'),
    url(r'^admin/', admin.site.urls),
    url(r'^robots\.txt$', include('robots.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap')
]
