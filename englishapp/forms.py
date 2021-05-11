from django import forms

class RegistrationForm(forms.Form):
    question = forms.CharField(max_length=100)
    answer = forms.CharField(max_length=100)
    category = forms.CharField(max_length=100)
