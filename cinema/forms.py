from django import forms
from django.contrib.auth.models import User
from cinema.models import Review, Film


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.TextInput(attrs={'class': 'form-control'}),
                   'password': forms.PasswordInput(attrs={'class': 'form-control'}), }


class ReviewForm(forms.ModelForm):
    stars = forms.IntegerField(max_value=5, min_value=0, required=True, help_text="How many stars out of 5?")
    review_text = forms.CharField(max_length=500, help_text="Write your review.")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Review
        exclude = ('user', 'IMDB_num', 'liked')


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ('IMDB_num', 'title', 'release', 'cast', 'director', 'age_rating', 'photo')
        widgets = {'IMDB_num': forms.TextInput(attrs={'class': 'form-control'}),
                   'title': forms.TextInput(attrs={'class': 'form-control'}),
                   'release': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
                   'cast': forms.TextInput(attrs={'class': 'form-control'}),
                   'director': forms.TextInput(attrs={'class': 'form-control'}),
                   'age_rating': forms.TextInput(attrs={'class': 'form-control'}),
                   'photo': forms.ClearableFileInput()}
