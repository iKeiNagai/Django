from django import forms
from .models import Flower, User, Competition

class Insertflower(forms.ModelForm):
    class Meta:
        model = Flower

class Insertuser(forms.ModelForm):
    class Meta:
        model = User

class Insertcompetition(forms.ModelForm):
    class Meta:
        model = Competition
        
class Dosearch(forms.Form):
    Search = forms.CharField()