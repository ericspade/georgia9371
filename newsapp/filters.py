import django_filters
from django.forms import DateInput
from django_filters import FilterSet
from .models import Post


class NewsFilter(FilterSet):
    header = django_filters.CharFilter(lookup_expr='icontains', label='Заголовок содержит:')
    release_year = django_filters.NumberFilter(field_name='time_in', lookup_expr='year__gt', label='Позже какого года?')

    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Post
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = ['header', 'category']
