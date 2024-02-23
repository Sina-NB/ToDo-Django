from django.contrib.auth.forms import AuthenticationForm
from django import forms

forms.ModelForm


class CustomAuthenticationForm(AuthenticationForm):
    """
    Custom authentication form that contains remember_me field
    """

    remember_me = forms.BooleanField(required=False)
