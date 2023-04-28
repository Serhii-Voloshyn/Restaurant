from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Avg
from datetime import datetime

from .serializers.EmployeeSerializers import EmployeeCreateSerializer
from .serializers.RestaurantSerializers import RestaurantSerializer
from .serializers.MenuSerializers import (
    MenuCreateSerializer, MenuListSerializer
)
from .serializers.MenuItemSerializers import MenuItemSerializer
from .serializers.VoteSerializers import VoteCreateSerializer

from .models import Menu, Vote, MenuItem, Restaurant, Employee


class CreateRestaurantView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = RestaurantSerializer


class RetrieveRestaurantView(generics.RetrieveAPIView):
    serializer_class = RestaurantSerializer

    def get(self, request, pk):
        response = self.get_serializer(
            get_object_or_404(Restaurant, id=pk)
        ).data
        return Response(response, status=status.HTTP_200_OK)


class CreateMenuView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = MenuCreateSerializer


class CreateMenuItemView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = MenuItemSerializer


class RetrieveMenuItemView(generics.RetrieveAPIView):
    serializer_class = MenuItemSerializer

    def get(self, request, pk):
        response = self.get_serializer(
            get_object_or_404(MenuItem, id=pk)
        ).data
        return Response(response, status=status.HTTP_200_OK)


class CreateEmployeeView(generics.CreateAPIView):
    serializer_class = EmployeeCreateSerializer


class CreateVoteView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = VoteCreateSerializer

    def post(self, request, menu_id):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        user = get_object_or_404(Employee, id=request.user.id)
        menu = get_object_or_404(Menu, id=menu_id)

        vote_exists = Vote.objects.filter(menu=menu, employee=user)
        if vote_exists:
            return Response(
                data={
                    'message': 'Already voted for this menu'
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save(employee=user, menu=menu)

        return Response(
            data={'message': 'Voted successfuly'},
            status=status.HTTP_200_OK
        )


class GetMenuCurrentDayView(generics.ListAPIView):
    serializer_class = MenuListSerializer
    queryset = Menu.objects.filter(date=datetime.now().date())

    def get(self, request, restaurant_id):
        date = datetime.now().date()
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        menu = Menu.objects.get(restaurant=restaurant, date=date)

        items = MenuItemSerializer(
            MenuItem.objects.filter(menu=menu),
            many=True
        )
        menu = self.get_serializer(menu)

        items = items.data
        menu = menu.data

        response = {
            'menu': menu,
            'items': items
        }
        return Response(data=response, status=status.HTTP_200_OK)


class GetVoteResultsCurrentDay(generics.ListAPIView):
    serializer_class = VoteCreateSerializer
    lookup_url_kwarg = 'menu_id'

    def get_queryset(self):
        menu_id = self.kwargs.get(self.lookup_url_kwarg)
        date = datetime.now().date()
        data = Vote.objects.filter(menu__id=menu_id, menu__date=date)
        return data


class GetAverageVoteResultsCurrentDay(generics.ListAPIView):
    serializer_class = VoteCreateSerializer
    lookup_url_kwarg = 'menu_id'

    def get(self, request, menu_id):
        response = self.get_queryset().aggregate(Avg('score'))
        return Response(data=response, status=status.HTTP_200_OK)

    def get_queryset(self):
        menu_id = self.kwargs.get(self.lookup_url_kwarg)
        date = datetime.now().date()
        data = Vote.objects.filter(menu__id=menu_id, menu__date=date)
        return data
