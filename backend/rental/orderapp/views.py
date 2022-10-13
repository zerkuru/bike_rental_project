import django.contrib.auth.models
from django.db.models import Q
from django.http import response, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission
from rest_framework.renderers import JSONRenderer

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from orderapp.filters import OrderFilter
from orderapp.models import Order
from orderapp.serializers import OrderSerializer, OrderSerializerPut


class IsAuthenticatedUser(BasePermission):
    def has_permission(self, request, view):
        if not isinstance(request.user, django.contrib.auth.models.AnonymousUser):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.user.id:
            return True
        return False


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.is_staff:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return True


class OrderView(ModelViewSet):
    model = Order
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticatedUser | IsAdmin]
    filterset_class = OrderFilter
    http_method_names = ['get', 'put', 'patch', 'head', 'options', 'trace', 'delete', 'post']

    def get_queryset(self):
        if isinstance(self.request.user, django.contrib.auth.models.AnonymousUser):
            return None
        elif self.request.user.is_superuser or self.request.user.is_staff:
            return Order.objects.all()
        else:
            return Order.objects.filter(user=self.request.user).all()
        # return Order.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return OrderSerializerPut
        return OrderSerializer

    def change_status(self, **kwargs):
        print('in change status')
        order = get_object_or_404(Order, pk=kwargs['pk'])
        order.status = kwargs['status']
        order.save()
        return HttpResponse(status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):

        order = get_object_or_404(Order, pk=kwargs['pk'])
        order.status = Order.CANCEL
        order.save()
        # response.accepted_renderer = JSONRenderer()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['user'] = Order.objects.values_list('user').filter(id=kwargs['pk']).first()[0]
        request.data._mutable = False
        return super().update(request, *args, **kwargs)


class MyTransportOrderView(ModelViewSet):
    model = Order
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticatedUser | IsAdmin]
    filterset_class = OrderFilter
    http_method_names = ['get', 'patch', 'head', 'options', 'trace']

    def get_queryset(self):
        if isinstance(self.request.user, django.contrib.auth.models.AnonymousUser):
            return None
        elif self.request.user.is_superuser or self.request.user.is_staff:
            return Order.objects.all()
        else:
            return Order.objects.filter(transport__transport_owner=self.request.user).all()
        # return Order.objects.all()
