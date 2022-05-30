from rest_framework import serializers
from .models import Cars

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cars
        fields = ('id', 'Manufacturer', 'Type', 'Model', 'Specs','Seller', 'Created_at', 'Updated_at')
