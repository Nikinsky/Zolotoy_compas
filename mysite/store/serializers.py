from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import *
from django.contrib.auth import authenticate
from django.db.models import Count


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['email', 'password', 'username', 'last_name', 'birth_date', 'phone_number', 'image']
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


# class LoginSerializers(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)
#
#     def validate(self, data):
#         user = authenticate(**data)
#         if user and user.is_active:
#             return user

class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'last_name', 'birth_date', 'phone_number', 'image']


class UserProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'last_name', 'image']





class RegionSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['region_name']


class RegionPhotosSerializers(serializers.ModelSerializer):
    class Meta:
        model = RegionPhotos
        fields = ['image']


class RegionSerializers(serializers.ModelSerializer):
    reg_photos = RegionPhotosSerializers(many=True)
    class Meta:
        model = Region
        fields = ['region_name', 'description', 'reg_photos']


class RegionFoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = RegionFood
        fields = ['region_food', 'food_name', 'include_food', 'description_name', 'image']












class PlacesPhotosSerializers(serializers.ModelSerializer):
    class Meta:
        model = PlacesPhotos
        fields = ['image']



class PlacesSerializers(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    places_photos = PlacesPhotosSerializers(many=True)
    class Meta:
        model = Places
        fields = ['places_name', 'description', 'average_rating', 'places_photos']

    def average_rating(self, obj):
        return obj.average_rating()


class PlacesListSerializers(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    places_photos = PlacesPhotosSerializers(many=True)
    class Meta:
        model = Places
        fields = ['places_name', 'average_rating', 'places_photos']

    def average_rating(self, obj):
        return obj.average_rating()

class PhotosReviewPlacesSerializers(serializers.ModelSerializer):
    class Meta:
        model = PhotosReview
        fields = ['image']

class ReviewSerializer(serializers.ModelSerializer):
    photos_review = PhotosReviewPlacesSerializers(many=True)
    author = UserProfileSimpleSerializers()
    class Meta:
        model = Review
        fields = ['author', 'rating', 'text', 'create_date', 'photos_review', 'like']



# class PlacesSimpleSerializer(serializers.ModelSerializer):
#     reviews = ReviewSerializer(many=True, read_only=True)
#     average_rating = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Places
#         fields = ['places_name', 'description', 'average_rating', 'reviews']
#
#
#     def get_average_rating(self, obj):
#         return obj.average_rating()











class HotelPhotosSerializers(serializers.ModelSerializer):
    class Meta:
        model = HotelPhotos
        fields = ['image']


class HotelSerializers(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    photos_hotel = HotelPhotosSerializers(many=True)

    class Meta:
        model = Hotel
        fields = ['places', 'hotel_name', 'address', 'average_rating', 'description', 'photos_hotel', 'offered_amenities', 'laest', 'short_period', 'medium_period', 'long_period', 'phone_number', 'bedroom', 'bathroom', 'car_bikes', 'pets_allow', ]


    def get_average_rating(self, obj):
        return obj.get_average_rating()



class ReviewPhotosHotelSerializers(serializers.ModelSerializer):
    class Meta:
        model = PhotosReviewHotel
        fields = ['image']


class ReviewHotelSerializer(serializers.ModelSerializer):
    photos_review_hotel = ReviewPhotosHotelSerializers(many=True)
    author = UserProfileSimpleSerializers()
    class Meta:
        model = ReviewHotel
        fields = ['author', 'rating', 'text', 'create_date', 'photos_review_hotel']



class HotelListSerializers(serializers.ModelSerializer):
    average_rating= serializers.SerializerMethodField()
    photos_hotel = HotelPhotosSerializers(many=True)

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'photos_hotel', 'average_rating' ]

    def get_average_rating(self, obj):
        return obj.get_average_rating()




class AttractionsPhotosSerializers(serializers.ModelSerializer):
    class Meta:
        model = AttractionsPhotos
        fields = ['image']

class AttractionSerializers(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    attraction_photos = AttractionsPhotosSerializers(many=True)
    class Meta:
        model = Attractions
        fields = ['at_name', 'description', 'attraction_photos', 'average_rating']


    def get_average_rating(self, obj):
        return obj.get_average_rating()


class ReviewPhotosAttractionSerializers(serializers.ModelSerializer):
    class Meta:
        model = PhotosReviewAttraction
        fields = ['image']


class ReviewAttractionSerializer(serializers.ModelSerializer):
    author = UserProfileSimpleSerializers()
    photos_review_attraction = ReviewPhotosAttractionSerializers(many=True)
    class Meta:
        model = ReviewAttraction
        fields = ['author', 'rating', 'text', 'create_date', 'photos_review_attraction']


class AttractionListSerializers(serializers.ModelSerializer):
    average_rating= serializers.SerializerMethodField()
    attraction_photos = AttractionsPhotosSerializers(many=True)

    class Meta:
        model = Attractions
        fields = ['at_name', 'attraction_photos', 'average_rating' ]

    def get_average_rating(self, obj):
        return obj.get_average_rating()







class KitchenPhotosSerializers(serializers.ModelSerializer):
    class Meta:
        model = KitchenPhotos
        fields = ['image']


class KitchenSerializers(serializers.ModelSerializer):
    kit_photos = KitchenPhotosSerializers(many=True)
    average_rating = SerializerMethodField()
    class Meta:
        model = Kitchen
        fields = ['name_kitchen', 'category', 'price_range', 'specialized_menu', 'meal_time', 'address', 'email', 'phone_number', 'average_rating',
                  'kit_photos']


    def get_average_rating(self, obj):
        return obj.get_average_rating()



class ReviewPhotosKitchenSerializers(serializers.ModelSerializer):
    class Meta:
        model = PhotosReviewKitchen
        fields = ['image']


class ReviewKitchenSerializers(serializers.ModelSerializer):
    author = UserProfileSimpleSerializers()
    photos_review_kitchen = ReviewPhotosKitchenSerializers(many=True)

    class Meta:
        model = ReviewKitchen
        fields = ['author', 'rating', 'text', 'create_date', 'photos_review_kitchen']


class KitchenListSerializers(serializers.ModelSerializer):
    average_rating= serializers.SerializerMethodField()
    kit_photos = AttractionsPhotosSerializers(many=True)

    class Meta:
        model = Kitchen
        fields = ['name_kitchen', 'kit_photos', 'average_rating' ]

    def get_average_rating(self, obj):
        return obj.get_average_rating()







class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user']


class CartItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['cart', 'places', 'hotel']









class CultureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Culture
        fields = ['id', 'culture_name', 'description', 'image']


class GamesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ['game_name', 'description', 'image']


class NationalClothesSerializers(serializers.ModelSerializer):
    class Meta:
        model = NationalClothes
        fields = ['clothes_name', 'description', 'image']

class HandCraftsSerializers(serializers.ModelSerializer):
    class Meta:
        model = HandCrafts
        fields = ['handcraft_name', 'description', 'image']

class CurrencySerializers(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['currency_name', 'description', 'image']


class NationalInstrumentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = NationalInstruments
        fields = ['instrument', 'description', 'image']



class NationalFoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = NationalFood
        fields = ['nationalfood_name', 'description', 'image']


