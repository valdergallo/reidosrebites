# encoding: utf-8
from django.views.generic import TemplateView


class LeadPageView(TemplateView):
    template_name = 'index.html'
