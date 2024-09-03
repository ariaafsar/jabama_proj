from django.shortcuts import render
from .models import Landlord
from .serializers import LandlordSerializer
from rest_framework.generics import ListAPIView

class SearchLandLordByName(ListAPIView) :
    queryset = Landlord.objects.all()
    serializer_class = LandlordSerializer
# Create your views here.
