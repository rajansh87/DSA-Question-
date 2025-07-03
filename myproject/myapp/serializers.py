# serializers.py
from rest_framework import serializers
from .models import User,Apartment
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'userId']

class ApartmentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Apartment
        fields = ['id','name', 'apartmentId', 'rent', 'rooms', 'date', 'location', 'category', 'user']