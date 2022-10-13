from django_filters import rest_framework as filters
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

