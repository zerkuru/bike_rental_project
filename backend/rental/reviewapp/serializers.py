from rest_framework import serializers

from authusersapp.serializers import UserModelSerializer
from transportapp.serializers import TransportSerializer
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    transport = TransportSerializer
    author = UserModelSerializer
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = '__all__'

