from rest_framework.serializers import ModelSerializer
from .models import UsersModel


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = UsersModel
        exclude = ['password']
        # fields = '__all__'