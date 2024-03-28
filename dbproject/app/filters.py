import django_filters
from django_filters import CharFilter
from .models import User

class thefilter(django_filters.FilterSet) :
    u_name = CharFilter(field_name= 'u_name', lookup_expr="icontains")
    class Meta:
        model = User
        fields = '__all__'
