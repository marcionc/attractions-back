from rest_framework.serializers import ModelSerializer
from core.models import TouristSpot
from rest_framework import serializers
from django.contrib.auth import authenticate

class TouristSpotSerializer(ModelSerializer):
    class Meta:
        model = TouristSpot
        fields = ('id', 'name', 'description')


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user and user.is_active:
            return {'user': user}
        raise serializers.ValidationError('Credenciais inválidas')