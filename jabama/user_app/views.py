from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.generics import ListAPIView

class SearchUserByName(ListAPIView) :
    queryset = User.objects.all()
    serializer_class = UserSerializer
# Create your views here.
