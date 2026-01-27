from .serializers import StoreSerializer, ProductSerializer
from .models import Store, Product
from rest_framework import generics, response, status

# Create your views here.


class StoreList(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class StoreDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    lookup_field = 'store_id'


class StoreDeleteAll(generics.DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        # Delete all Store objects
        Store.objects.all().delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


class ProductDeleteAll(generics.DestroyAPIView):
    def delete(self, request, *args, **kwargs):
        Product.objects.all().delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

