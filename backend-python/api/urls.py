from django.urls import path

from .views.city.city_views import CityDetail
from .views.city.city_get_list import CityList
from .views.mountain.mountain_get_list import MountainList
from .views.mountain.mountain_views import MountainDetail
from .views.river.river_get_list import RiverList
from .views.river.river_views import RiverDetail

urlpatterns = [
    path('city', CityList.as_view(), name='city-list'),
    path('city/<int:pk>', CityDetail.as_view(), name='city-details'),
    path('river', RiverList.as_view(), name='river-list'),
    path('river/<int:pk>', RiverDetail.as_view(), name='river-details'),
    path('mountain', MountainList.as_view(), name='mountain-list'),
    path('mountain/<int:pk>', MountainDetail.as_view(), name='mountain-details')
]
