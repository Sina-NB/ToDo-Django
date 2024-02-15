from django.contrib.auth.forms import AuthenticationForm
from django import forms

forms.ModelForm
class CustomAuthenticationForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False)
