from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=50)
    password = forms.CharField(min_length=3, max_length=50)
