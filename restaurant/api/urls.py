from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import (
    CreateEmployeeView, CreateMenuView, CreateRestaurantView, CreateMenuItemView,
    GetMenuCurrentDayView, GetVoteResultsCurrentDay, CreateVoteView,
    RetrieveMenuItemView, RetrieveRestaurantView, GetAverageVoteResultsCurrentDay
)


urlpatterns = [
    path('api/create_employee', CreateEmployeeView.as_view(), name='create_employee'),
    path('api/create_restaurant', CreateRestaurantView.as_view(), name='create_restaurant'),
    path('api/retrieve_restaurant/<int:pk>', RetrieveRestaurantView.as_view(), name='retrieve_restaurant'),
    path('api/create_menu', CreateMenuView.as_view(), name='create_menu'),
    path('api/create_menu_item', CreateMenuItemView.as_view(), name='create_menu_item'),
    path('api/retrieve_menu_item/<int:pk>', RetrieveMenuItemView.as_view(), name='retrieve_menu_item'),
    path('api/vote/<int:menu_id>', CreateVoteView.as_view(), name='create_vote'),

    path('api/get_menu_current_day/<int:restaurant_id>', GetMenuCurrentDayView.as_view(), name='get_menu_current_day'),
    path('api/get_votes_current_day/<int:menu_id>', GetVoteResultsCurrentDay.as_view(), name='get_votes_current_day'),
    path('api/get_avg_votes_current_day/<int:menu_id>', GetAverageVoteResultsCurrentDay.as_view(), name='get_avg_votes_current_day'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]