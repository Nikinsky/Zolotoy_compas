from django_filters import FilterSet
from .models import *


class PlacesFilter(FilterSet):
    class Meta:
        model = Places
        fields = {
            'region_places': ['exact'],
            'places_name': ['exact'],
        }


# class ReviewPlacesFilter(FilterSet):
#     class Meta:
#         model = Places
#         fields = {
#             'author': ['exact'],
#         }


class HotelFilter(FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'places': ['exact'],
            'hotel_name': ['exact'],
        }


class KitchenFilter(FilterSet):
    class Meta:
        model = Kitchen
        fields = {
            'places': ['exact'],
            'name_kitchen': ['exact'],
        }

class AttractionFilter(FilterSet):
    class Meta:
        model = Attractions
        fields = {
            'att_region': ['exact'],
            'at_name': ['exact'],
        }