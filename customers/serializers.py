from rest_framework import serializers
from .models import Customer

class CustomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = ('pk', 'first_name', 'last_name', 'email', 'phone', 'address', 'description')