from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Property
from .serializers import PropertySerializer

class SearchPropertyByName(ListAPIView) :
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
# Create your views here.
