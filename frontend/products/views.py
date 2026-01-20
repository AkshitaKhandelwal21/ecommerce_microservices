from django.shortcuts import render
from django.views.generic import TemplateView

from services.product_client import get_all_products

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = get_all_products()
        return context
        