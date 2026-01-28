from django.shortcuts import render
from django.views.generic import TemplateView

from services.product_client import ProductService, get_all_products

# Create your views here.
class HomeView(TemplateView):
    template_name = 'users/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subcats'] = ProductService.get_subcat()
        context['products'] = ProductService.get_products({'limit': 10})
        return context
        

class ProductList(TemplateView):
    template_name = 'products/product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # sub = self.kwargs.get('sub')
        filters = self.request.GET.dict()
        context['products'] = ProductService.get_products(filters)
        context['subcats'] = ProductService.get_subcat()

        return context
    

# class SubCategoryListView(TemplateView):
#     template_name = 'products/product_list.html'

#     def get_context_data(self, **kwargs):
#         sub = self.kwargs.get('sub')
#         context = super().get_context_data(**kwargs)
#         context['products'] = ProductService.get_product_by_subcategory(sub)
#         return context
    