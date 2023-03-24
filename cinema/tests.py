from django.contrib.auth.models import User
from django.urls import reverse

from cinema.models import Film
from django.test import TestCase
from datetime import datetime


# Create your tests here.
def add_user(username, email, password):
    new_user = User()

    new_user.username = username
    new_user.email = email
    new_user.password = password
    new_user.save()

    return new_user


def add_film(IMDB_num, title, release, cast, director, age_rating):

    new_film = Film(IMDB_num=IMDB_num, title=title, release=release,
                    cast=cast, director=director, age_rating=age_rating)

    return new_film


def make_user_john():
    add_user("JohnDaGoat12", "johnnyb2003@gmail.com", "John12345")


def make_film_goldfinger():
    return add_film(123456789, "Goldfinger", datetime.strptime("1964-09-17", "%Y-%m-%d").date(),
             "Sean Connery", "Guy Hamilton", "PG")


class UserTests(TestCase):

    def test_user_has_username(self):
        make_user_john()
        self.assertTrue(User.objects.filter(username="JohnDaGoat12").exists())

    def test_user_has_email(self):
        make_user_john()
        self.assertTrue(User.objects.filter(email="johnnyb2003@gmail.com").exists())

    def test_user_has_password(self):
        make_user_john()
        self.assertTrue(User.objects.filter(password="John12345").exists())

    def test_user_redirected(self):
        film = make_film_goldfinger()
        response = self.client.get(f"/cinema/reviews/{film.IMDB_num}/leave_review")
        self.assertEquals(response.status_code, 301)
