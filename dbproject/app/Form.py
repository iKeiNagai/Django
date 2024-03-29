from django import forms
from .models import Flower, User, Competition

#forms connected to models include all fields
class Insertflower(forms.ModelForm):
    class Meta:
        model = Flower
        fields = "__all__"

class Insertuser(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

class Insertcompetition(forms.ModelForm):
    class Meta:
        model = Competition
        fields = "__all__"
        
class Dosearch(forms.Form):
    Search = forms.CharField()