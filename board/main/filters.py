import django_filters
from django_filters import FilterSet
from .models import Reply


# Создаем свой набор фильтров для модели
class ReplyFilter(FilterSet):
    ads__title = django_filters.CharFilter(lookup_expr='icontains')
   
    class Meta:
        model = Reply
        fields = ['ads__title', ]