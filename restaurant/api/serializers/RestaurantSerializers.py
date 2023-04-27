from rest_framework import serializers
from ..models import Restaurant


class RestaurantSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150)
    location = serializers.CharField(max_length=250)

    class Meta:
        model = Restaurant
        fields = ['name', 'location']
