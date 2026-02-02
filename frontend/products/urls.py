from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('products/', views.ProductList.as_view(), name='products'),
    path('new_product/', views.NewProductView.as_view(), name='new-product'),
    # path('<str:sub>/', views.SubCategoryListView.as_view(), name='subcat'),
    # path('/')
]