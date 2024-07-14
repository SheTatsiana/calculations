from django import forms
from .models import Room, Building

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'length', 'width']

class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = ['name', 'rooms']
    rooms = forms.ModelMultipleChoiceField(queryset=Room.objects.all(), widget=forms.CheckboxSelectMultiple)
