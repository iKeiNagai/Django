import django_filters
from django_filters import CharFilter, NumberFilter, ChoiceFilter
from .models import User, Organizers, Competition, Flower

class thefilter(django_filters.FilterSet) : #filter querysets

    #filter field u_name from user model, if contains input it gets it
    u_name = CharFilter(field_name= 'u_name', lookup_expr="icontains", label='Participant Name')
    u_id = NumberFilter(field_name= 'u_id', label='Participant ID')
    class Meta:
        model = User 
        fields = ['u_name',
                  'u_id'] #fields to filter(for form)

class OrganizersFilter(django_filters.FilterSet) :
    o_id = NumberFilter(field_name='o_id', lookup_expr="exact", label='Organizer ID')
    o_name = CharFilter(field_name='o_name', lookup_expr='icontains', label='Organizer Name')
    specialty = CharFilter(field_name='specialty', lookup_expr='icontains', label='Specialty')
    class Meta: 
        model = Organizers
        fields = '__all__'

class CompetitionsFilter(django_filters.FilterSet) :
    c_id = NumberFilter(field_name='c_id', lookup_expr='exact', label='Competition ID')
    c_name = CharFilter(field_name='c_name', lookup_expr='icontains', label='Competition Name')
    c_location = CharFilter(field_name='c_location', lookup_expr='icontains', label='Location')
    class Meta:
        model = Competition
        fields = ['c_id',
                  'c_name',
                  'c_location']

class entriesFilter(django_filters.FilterSet):
    species = CharFilter(field_name='species', lookup_expr='icontains', label='Flower Species')
    color = CharFilter(field_name='color',lookup_expr='exact',label='Flower Color')
    class Meta:
        model = Flower
        fields = ['species',
                  'color']