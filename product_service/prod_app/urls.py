from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter(trailing_slash=False)
# router.register('', Products, basename='prod')

urlpatterns = [
    # path('products/', include(router.urls)),
   path('products/', views.ProductsView.as_view(), name='products'), 
   path('product/<int:pk>/', views.ProductsByIdView.as_view(), name='product'),
   path('category/', views.CategoryView.as_view(), name='category')
#    path('subcategory/', views)
]
