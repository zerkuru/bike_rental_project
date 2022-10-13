from django_filters import rest_framework as filters

from orderapp.models import Order
from transportapp.models import TransportModel


class TransportFilter(filters.FilterSet):
    max_price = filters.NumberFilter(field_name='rental_price', lookup_expr='lte')
    min_price = filters.NumberFilter(field_name='rental_price', lookup_expr='gte')
    max_age_limit = filters.NumberFilter(field_name='age_limit', lookup_expr='lte')
    min_age_limit = filters.NumberFilter(field_name='age_limit', lookup_expr='gte')
    deposit = filters.BooleanFilter(field_name='deposit', lookup_expr='isnull')

    class Meta:
        model = TransportModel
        fields = ['transport_type']


class OrderFilter(filters.FilterSet):
    date_from = filters.DateTimeFilter(field_name='date_from', lookup_expr='gte')
    date_to = filters.DateTimeFilter(field_name='date_to', lookup_expr='lte')
    status = filters.ChoiceFilter(field_name='status')

    class Meta:
        model = Order
        fields = ['date_from', 'date_to', 'status']
