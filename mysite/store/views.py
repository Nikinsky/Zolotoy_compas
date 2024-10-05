from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from .filters import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter



class UserProfileView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers





class RegionView(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializers


class RegionPhotosView(viewsets.ModelViewSet):
    queryset = RegionPhotos.objects.all()
    serializer_class = RegionPhotosSerializers


class RegionFoodView(viewsets.ModelViewSet):
    queryset = RegionFood.objects.all()
    serializer_class = RegionFoodSerializers







class PlacesViewSet(viewsets.ModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlacesSerializers




class PlacesPhotosView(viewsets.ModelViewSet):
    queryset = PlacesPhotos.objects.all()
    serializer_class = PlacesPhotosSerializers

class PlacesListView(viewsets.ModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlacesListSerializers
    filterset_class = PlacesFilter

class ReviewView(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # filterset_class = ReviewPlacesFilter






class AttractionsView(viewsets.ModelViewSet):
    queryset = Attractions.objects.all()
    serializer_class = AttractionSerializers
    filterset_class = AttractionFilter


class ReviewAttractionView(viewsets.ModelViewSet):
    queryset = ReviewAttraction.objects.all()
    serializer_class = ReviewAttractionSerializer


class AttractionListView(viewsets.ModelViewSet):
    queryset = Attractions.objects.all()
    serializer_class = AttractionListSerializers
    filterset_class = AttractionFilter









class HotelView(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializers


class ReviewHotelView(viewsets.ModelViewSet):
    queryset = ReviewHotel.objects.all()
    serializer_class = ReviewHotelSerializer

class HotelListView(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializers
    filterset_class = HotelFilter







class KitchenView(viewsets.ModelViewSet):
    queryset = Kitchen.objects.all()
    serializer_class = KitchenSerializers

class ReviewKitchenView(viewsets.ModelViewSet):
    queryset = ReviewKitchen.objects.all()
    serializer_class = ReviewKitchenSerializers

class KitchenListView(viewsets.ModelViewSet):
    queryset = Kitchen.objects.all()
    serializer_class = KitchenListSerializers
    filterset_class = KitchenFilter







class CartView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers

class CartItemsView(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializers






class CultureView(viewsets.ModelViewSet):
    queryset = Culture.objects.all()
    serializer_class = CultureSerializers


class GamesView(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesSerializers


class NationalClothesView(viewsets.ModelViewSet):
    queryset = NationalClothes.objects.all()
    serializer_class = NationalClothesSerializers


class HandCraftSerializers(viewsets.ModelViewSet):
    queryset = HandCrafts.objects.all()
    serializer_class = HandCraftsSerializers


class CurrencyView(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializers


class NationalInstrumentsView(viewsets.ModelViewSet):
    queryset = NationalInstruments.objects.all()
    serializer_class = NationalInstrumentsSerializers

class NationalFoodView(viewsets.ModelViewSet):
    queryset = NationalFood.objects.all()
    serializer_class = NationalFoodSerializers