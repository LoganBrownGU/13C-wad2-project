from django import forms
from django.contrib.auth.models import User
from cinema.models import Review


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class ReviewForm(forms.ModelForm):
    stars = forms.IntegerField(max_value=5, min_value=0, required=True, help_text="How many stars out of 5?")
    review_text = forms.CharField(max_length=500, help_text="Write your review.")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    dislikes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Review

        exclude = ('user', 'IMDB_num',)
        fields = ('username', 'email', 'password',)
