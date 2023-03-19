from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.TextInput(attrs={'class': 'form-control'}),
                   'password': forms.PasswordInput(attrs={'class': 'form-control'}),}
