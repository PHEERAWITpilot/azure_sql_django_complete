from rest_framework import generics
from django.contrib.auth.models import User
from ..serializers import UserSerializer

class UserList(generics.ListCreateAPIView):
    # API view to list and create users
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    # API view to retrieve, update or delete a user instance
    queryset = User.objects.all()
    serializer_class = UserSerializer
