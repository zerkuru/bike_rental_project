from django_filters import rest_framework

from .models import Order


class OrderFilter(rest_framework.FilterSet):
    date_from = rest_framework.DateTimeFilter(field_name='date_from', lookup_expr='gte')
    date_to = rest_framework.DateTimeFilter(field_name='date_to', lookup_expr='lte')
    status = rest_framework.ChoiceFilter(field_name='status')

    class Meta:
        model = Order
        fields = ['date_from', 'date_to', 'status']

