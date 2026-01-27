from django.db import models

# Create your models here.

class TimeStamps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)


class SubCategory(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, 
                                 related_name="subcategory")
    
    class Meta:
        unique_together = ('name', 'category')

class ProductModel(TimeStamps, models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    desc = models.TextField()
    price = models.FloatField()
    seller_id = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT)

class ProductImage(TimeStamps, models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, 
                                related_name='images')
    image_url = models.URLField()


