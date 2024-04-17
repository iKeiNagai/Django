from django import forms
from .models import Flower, User, Competition, Organizers

#forms connected to models include all fields
class Insertflower(forms.ModelForm):
    class Meta:
        model = Flower
        fields = "__all__"
        labels = {
            'species' : 'Flower Species',
            'size' : 'Flower Size',
            'color' : 'Flower Color',
            'age' : 'Flower Age'
        }

class Insertuser(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        labels = {
            'u_name' : 'Name',
            'u_address' : 'Home Address',
            'entriesno' : 'Entries No'
        }

class Insertcompetition(forms.ModelForm):
    class Meta:
        model = Competition
        fields = "__all__"
        labels = {
            'c_name' : 'Competition Name',
            'c_location' : 'Location',
            'c_date' : 'Date (yyyy/mm/dd time)',
            'participantsno' : 'Participants No'
        }

class InsertOrganizer(forms.ModelForm):
    class Meta:
        model = Organizers
        fields = "__all__"
        labels = {
            'o_name' : 'Organizer Name',
            'specialty' : 'Organizer Specialty'
        }

class randc(forms.Form):
    Name = forms.CharField(label="name")
    PersonNo = forms.IntegerField(label="NNumber")

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['u_name', 'u_address', 'entriesNo']

class OrganizerUpdateForm(forms.ModelForm):
    class Meta:
        model = Organizers
        fields = ['o_name', 'specialty']

class CompetitionUpdateForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ['c_name', 'c_location', 'c_date']