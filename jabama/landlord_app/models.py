from django.db import models
from property_app.models import Property
# Create your models here.
class Landlord(models.Model) :
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    properties = models.ForeignKey(Property, on_delete=models.CASCADE)
    