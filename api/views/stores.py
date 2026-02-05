from rest_framework import generics, response, status
from ..models import Store
from ..serializers import StoreSerializer

class StoreList(generics.ListCreateAPIView):
    # API view to retrieve list of stores or create a new store
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class StoreDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    # API view to retrieve, update or delete a store instance
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    lookup_field = 'store_id'

class StoreDeleteAll(generics.DestroyAPIView):
    # API view to delete all stores
    def delete(self, request, *args, **kwargs):
        # Delete all Store objects
        Store.objects.all().delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
