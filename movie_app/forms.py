from django import forms
from matplotlib import widgets
from .models import Movie

class NewForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields= ['name', 'rating', 'year', 'budget']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'budget': forms.NumberInput(attrs={'class': 'form-control'})
        }
