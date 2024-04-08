import django_filters
from django_filters import CharFilter, NumberFilter
from .models import User, Organizers

class thefilter(django_filters.FilterSet) : #filter querysets

    #filter field u_name from user model, if contains input it gets it
    u_name = CharFilter(field_name= 'u_name', lookup_expr="icontains")
    
    class Meta:
        model = User 
        fields = '__all__' #fields to filter(for form)

class OrganizersFilter(django_filters.FilterSet) :
    o_id = NumberFilter(field_name='o_id', lookup_expr="exact")
    class Meta: 
        model = Organizers
        fields = '__all__'