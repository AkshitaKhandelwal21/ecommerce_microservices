from http.client import HTTPException
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from prod_app.models import Category, ProductModel, SubCategory
from prod_app.serializer import CategorySerializer, ProductSerializer, SubCategorySerializer

# Create your views here.

    # class Products(viewsets.ModelViewSet):
    #     queryset = ProductModel.objects.all()
    #     serializer_class = ProductSerializer

class ProductsView(APIView):
    try:
        def get(self, request):
            queryset = ProductModel.objects.all()
            sub = request.GET.get('sub')

            if sub:
                queryset = ProductModel.objects.filter(sub_category__name=sub)

            serializer = ProductSerializer(queryset, many=True)
            return Response(serializer.data)

        def post(self, request):
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

    except Exception as e:
        raise HTTPException(e)
            

class ProductsByIdView(APIView):
    def get_object(self, request, pk):
        product = ProductModel.objects.get(pk=pk)
        return product
    
    def get(self, request, pk):
        product = self.get_object(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk):
            product = self.get_object(pk=pk)
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
    
    def delete(self, request, pk):
        product = self.get_object(pk=pk)
        product.delete()
        

class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class SubCategoryView(APIView):
    def get(self, request):
        subs = SubCategory.objects.all()
        serializer = SubCategorySerializer(subs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SubCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class SubcatById(APIView):
    def get_object(self, request, pk):
        sub = SubCategory.objects.get(pk=pk)
        return sub
    
    def get(self, request, pk):
        sub = self.get_object(pk)
        serializer = SubCategorySerializer(sub)
        return Response(serializer.data)
    
    def put(self, request, pk):
        sub = self.get_object(pk=pk)
        serializer = SubCategorySerializer(sub, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, pk):
        sub = self.get_object(pk=pk)
        sub.delete()


class ProductbySubcategory(APIView):
    def get(self, request, sub):
        queryset = ProductModel.objects.filter(sub_category__name=sub)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)