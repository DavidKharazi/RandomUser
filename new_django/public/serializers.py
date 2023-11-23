from rest_framework import serializers
from .models import RandomUser

class RandomUserSerializer(serializers.Serializer):
    gender = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    street_number = serializers.IntegerField(read_only=True)
    street_name = serializers.CharField(read_only=True)
    city = serializers.CharField(read_only=True)
    country = serializers.CharField(read_only=True)
    postcode = serializers.CharField(read_only=True)
    login = serializers.CharField(read_only=True)
    password = serializers.CharField(read_only=True)
    born_data = serializers.CharField(read_only=True)
    age = serializers.IntegerField(read_only=True)
