from django.urls import re_path, path

from .views import city_views
from .views import mountain_views
from .views import river_views

urlpatterns = [
    path('city', city_views.CityList.as_view(), name='city-list'),
    path('city/<int:pk>', city_views.CityDetail.as_view(), name='city-details'),
    path('river', river_views.RiverList.as_view(), name='river-list'),
    path('river/<int:pk>', river_views.RiverDetail.as_view(), name='river-details'),
    path('mountain', mountain_views.MountainList.as_view(), name='mountain-list'),
    path('mountain/<int:pk>', mountain_views.MountainDetail.as_view(), name='mountain-details')
]
