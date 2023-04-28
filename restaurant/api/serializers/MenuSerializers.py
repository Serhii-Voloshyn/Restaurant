from rest_framework import serializers
from ..models import Menu


class MenuCreateSerializer(serializers.ModelSerializer):
    date = serializers.DateField()

    class Meta:
        model = Menu
        fields = ['date', 'restaurant']


class MenuListSerializer(serializers.ModelSerializer):
    date = serializers.DateField()
    restaurant = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='retrieve_restaurant',
    )

    class Meta:
        model = Menu
        fields = ['date', 'restaurant']
