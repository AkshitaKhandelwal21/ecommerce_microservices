from django.contrib import admin

from prod_app.models import ProductModel, Category, SubCategory, ProductImage

# Register your models here.
admin.site.register(ProductModel)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(SubCategory)