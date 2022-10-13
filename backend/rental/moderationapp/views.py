from django.shortcuts import render
from rest_framework.permissions import BasePermission, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from authusersapp.models import UsersModel
from authusersapp.serializers import UserModelSerializer
from orderapp.models import Order
from orderapp.serializers import OrderSerializer
from transportapp.models import TransportModel, ManufacturerModel, TransportTypeModel
from transportapp.serializers import TransportSerializer, ManufacturerSerializer, TransportTypeSerializer


class IsSuperUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class StaffViewSet(ModelViewSet):
    admin_permissions = ['list', 'update', 'retrieve', 'create']

    def get_permissions(self):
        if self.action in self.admin_permissions:
            permission_classes = [IsAdminUser, IsSuperUser]
        else:
            permission_classes = [IsSuperUser]
        return [permission() for permission in permission_classes]


class TransportModViewSet(StaffViewSet):
    serializer_class = TransportSerializer
    queryset = TransportModel.objects.all()


class TransportTypeModViewSet(StaffViewSet):
    serializer_class = TransportTypeSerializer
    queryset = TransportTypeModel.objects.all()


class ManufacturerModViewSet(StaffViewSet):
    serializer_class = ManufacturerSerializer
    queryset = ManufacturerModel.objects.all()


class UserModViewSet(StaffViewSet):
    serializer_class = UserModelSerializer
    queryset = UsersModel.objects.all()


class OrderModViewSet(StaffViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

