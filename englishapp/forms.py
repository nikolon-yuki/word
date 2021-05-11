from django import forms

class RegistrationForm(forms.Form):
    question = forms.CharField('問題',max_length=100)
    answer = forms.CharField('答え',max_length=100)
