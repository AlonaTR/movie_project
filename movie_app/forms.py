from django import forms
from .models import Movie

class NewForm(forms.Form):
    name = forms.CharField(max_length=40)
    rating = forms.IntegerField()
    year = forms.IntegerField(null=True)
    budget= forms.IntegerField(default=10000000)