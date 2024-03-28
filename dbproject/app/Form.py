from django import forms
from .models import Flower, User

class Insertflower(forms.Form):
    species = forms.CharField(max_length=30)
    size = forms.FloatField()
    color = forms.CharField(max_length=10)
    age = forms.IntegerField(min_value=16,max_value=100)
    class Meta:
        model = Flower

class Insertuser(forms.Form):
    u_name = forms.CharField(max_length=30)
    u_address = forms.CharField(max_length=30)
    entriesno = forms.IntegerField()
    class Meta:
        model = User

class Insertcompetition(forms.Form):
    c_name = forms.CharField(max_length=50)
    c_location = forms.CharField(max_length=30)
    c_date = forms.DateTimeField()
    participantno = forms.IntegerField()

class Dosearch(forms.Form):
    Search = forms.CharField()