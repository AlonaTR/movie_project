import re
from django import forms
from .models import Movie

class NewForm(forms.Form):
    name = forms.CharField(max_length=40)
    rating = forms.IntegerField(required=False)
    year = forms.IntegerField()
    budget= forms.IntegerField()