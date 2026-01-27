from rest_framework import serializers

from prod_app.models import Category, ProductImage, ProductModel, SubCategory


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image_url']


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = ProductModel
        fields = '__all__'


    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        product = ProductModel.objects.create(**validated_data)
        for image in images_data:
            ProductImage.objects.create(product=product, **image)
        return product
    
    def update(self, instance, validated_data):
        images_data = validated_data.pop('images', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if images_data:
            instance.image.all().delete()
            for image in images_data:
                ProductImage.objects.create(product=instance, **image)

        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"
        

