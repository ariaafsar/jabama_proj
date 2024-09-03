from django.db import models

class property(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    owner = models.ForeignKey('Landlord', on_delete=models.CASCADE)
# Create your models here.
