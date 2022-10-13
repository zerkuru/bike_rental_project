from rest_framework import serializers

from authusersapp.serializers import UserModelSerializer
from .models import TransportModel, TransportTypeModel, ManufacturerModel


# class TransportTypeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TransportTypeModel
#         fields = '__all__'
#
#
# class ManufacturerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ManufacturerModel
#         fields = '__all__'
#
#
# class TransportSerializer(serializers.ModelSerializer):
#     transport_type = TransportTypeSerializer
#     manufacturer = ManufacturerModel
#
#     class Meta:
#         model = TransportModel
#         fields = '__all__'

# Вариант для получения имен пользователя, типа и производителя транспорта вместо id
class TransportSerializer(serializers.ModelSerializer):
    transport_owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = TransportModel
        fields = '__all__'

    def to_representation(self, instance):
        rep = super(TransportSerializer, self).to_representation(instance)
        rep['transport_type'] = instance.transport_type.name
        rep['manufacturer'] = instance.manufacturer.name
        rep['transport_owner'] = instance.transport_owner.full_name
        return rep


class TransportTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportTypeModel
        fields = '__all__'


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManufacturerModel
        fields = '__all__'