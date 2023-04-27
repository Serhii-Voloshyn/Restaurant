from rest_framework import serializers
from ..models import MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=500)
    price = serializers.FloatField()
    weight = serializers.IntegerField()

    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'weight', 'menu']