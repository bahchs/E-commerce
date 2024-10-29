from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Category,Product,Variation
from .serializers import CategorySerializer, ProductSerializer,VariationSerializer

# Create your views here.
def index(request):
    items=Variation.objects.all()
    return render(request, 'homeshop/index.html', {"items":items})

def viewShop(request):
    items=Variation.objects.all()
    return render(request, 'homeshop/shop.html', {"items":items})

def viewItem(request, id):
    item = get_object_or_404(Variation, id=id)
    return render(request, 'homeshop/item.html', {"item":item})

class GetCategoryAPI(APIView):
    def get(self,request):
        list_category=Category.objects.all()
        mydata = CategorySerializer(list_category, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)
    
    def post(self,request):
        mydata = CategorySerializer(data=request.data)
        if not mydata.is_valid():
            return Response({'error': 'Data error'}, status=status.HTTP_400_BAD_REQUEST)
        validated_data = mydata.validated_data
        cate = Category.objects.create(**validated_data)
        created_category = CategorySerializer(cate)
        return Response(data=created_category.data, status=status.HTTP_200_OK)
    
    def put(self,request, id):
        category= get_object_or_404(Category, id=id)
        mydata=CategorySerializer(category, data=request.data)
        if mydata.is_valid():
            mydata.save()
            return Response(data=mydata.data, status=status.HTTP_200_OK)
        return Response({'error': 'Data error'}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, id):
        try:
            category=Category.objects.get(id=id)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response({'message': 'Category deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class GetProductAPI(APIView):
    def get(self, request):
        list_product=Product.objects.all()
        mydata= ProductSerializer(list_product, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        mydata= ProductSerializer(data=request.data)
        if not mydata.is_valid():
            return Response({'error': 'Data error'}, status=status.HTTP_400_BAD_REQUEST)
        validated_data = mydata.validated_data
        item=Product.objects.create(**validated_data)
        create_item=ProductSerializer(item)
        return Response(data=create_item.data, status=status.HTTP_200_OK)
    
    def put(self,request, id):
        product=get_object_or_404(Product, id=id)
        mydata=ProductSerializer(product,data=request.data)
        if mydata.is_valid():
            mydata.save()
            return Response(data=mydata.data, status=status.HTTP_200_OK)
        return Response({'error': 'Data error'}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        try:
            product=Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response({'message': 'Category deleted successfully'}, status=status.HTTP_204_NO_CONTENT)




