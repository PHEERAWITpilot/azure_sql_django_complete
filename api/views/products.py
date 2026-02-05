from rest_framework import generics, response, status
from ..models import Product
from ..serializers import ProductSerializer

class ProductList(generics.ListCreateAPIView):
    # API view to retrieve list of products or create a new product
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    # API view to retrieve, update or delete a product instance
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class ProductDeleteAll(generics.DestroyAPIView):
    # API view to delete all products
    def delete(self, request, *args, **kwargs):
        Product.objects.all().delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
