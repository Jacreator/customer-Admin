import django_filters
from django_filters import DateFilter
from .models import *


class OrderFilter(django_filters.FilterSet):
    star_date = DateFilter(field_name="date", lookup_expr='gte')
    end_dates = DateFilter(field_name="date", lookup_expr='get', logout=)

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date']
