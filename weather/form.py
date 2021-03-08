from django import forms
from .models import weather_data

class search_bar(forms.ModelForm):
    class Meta:
        model = weather_data
        fields = ['location']
        widgets = {
        'location': forms.TextInput(attrs={'class': 'searchbar', 'placeholder': 'Search'})
        }