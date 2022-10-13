from rest_framework import serializers

from authusersapp.serializers import UserModelSerializer
from transportapp.serializers import TransportSerializer
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    transport = TransportSerializer
    user = UserModelSerializer
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    date_from = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S', input_formats=['%Y-%m-%d %H:%M:%S'])
    date_to = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S', input_formats=['%Y-%m-%d %H:%M:%S'])

    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):

        rep = super(OrderSerializer, self).to_representation(instance)
        rep['transport_price'] = instance.transport.rental_price
        rep['status'] = self.name_of_status(instance.status)
        rep['client_name'] = instance.user.full_name
        rep['client_phone'] = instance.user.tel_number
        rep['client_email'] = instance.user.email
        rep['transport_owner'] = instance.transport.transport_owner.full_name
        rep['transport_owner_phone'] = instance.transport.transport_owner.tel_number
        rep['transport_owner_email'] = instance.transport.transport_owner.email
        return rep

    def name_of_status(self, status):
        for item in Order.ORDER_STATUS:
            if status in item:
                return item[1]


class OrderSerializerPut(serializers.ModelSerializer):
    transport = TransportSerializer
    user = UserModelSerializer
    date_from = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S', input_formats=['%Y-%m-%d %H:%M:%S'])
    date_to = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S', input_formats=['%Y-%m-%d %H:%M:%S'])

    class Meta:
        model = Order
        fields = '__all__'
