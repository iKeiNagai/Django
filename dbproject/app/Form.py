from django import forms
from .models import Flower, User, Competition, Organizers

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

class InsertOrganizer(forms.ModelForm):
    class Meta:
        model = Organizers
        fields = "__all__"

class randc(forms.Form):
    Name = forms.CharField(label="name")
    PersonNo = forms.IntegerField(label="NNumber")