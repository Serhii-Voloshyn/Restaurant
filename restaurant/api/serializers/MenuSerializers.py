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
    menu_items = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='retrieve_menu_item',
    )

    class Meta:
        model = Menu
        fields = ['date', 'restaurant', 'menu_items']