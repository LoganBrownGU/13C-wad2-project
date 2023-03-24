from django.contrib.auth.models import User
from cinema.models import Review, Film

from django.test import TestCase
from django.urls import reverse


# Create your tests here.
def add_user(username, email, password):
    new_user = User()
    new_user.username = username
    new_user.email = email
    new_user.password = password
    new_user.save()

    return new_user

def add_film(IMDB_num, title, release, cast, director, age_rating):
    new_film = Film()
    new_film.IMDB_num = IMDB_num
    new_film.title = title
    new_film.release = release
    new_film.cast = cast
    new_film.director = director
    new_film.age_rating = age_rating
    new_film.save()

    return new_user


def make_user_john():
    add_user("JohnDaGoat12", "johnnyb2003@gmail.com", "John12345")
    
def make_film():
    add_film("tt001", "The best movie", 2000-11-11, "John", "John", "10")


class UserTests(TestCase):

    def test_user_exists(self):
        make_user_john()
        self.assertTrue(User.objects.filter(username="JohnDaGoat12").exists())

    # def test_user_redirected(self):
    #     response = self.client.get(reverse("cinema:manager"))
    #     self.assertEquals(response.status_code, 302)
