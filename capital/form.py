from django import forms
from .models import country_data

class search_bar(forms.ModelForm):
    class Meta:
        model = country_data
        fields = ['country']
        widgets = {
        'country': forms.TextInput(attrs={'class': 'searchbar', 'placeholder': 'Search'})
        }