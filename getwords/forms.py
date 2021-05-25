from django import forms
from django.conf import settings

class InputWordsForm(forms.Form):
    spell = forms.CharField(max_length=100)