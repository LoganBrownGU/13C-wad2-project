from django.contrib.auth.models import User
from cinema.models import Film, Review
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
    return add_user("JohnDaGoat12", "johnnyb2003@gmail.com", "John12345")


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

def add_film(IMDB_num, title, release, cast, director, age_rating):
    new_film = Film()
    new_film.IMDB_num = IMDB_num
    new_film.title = title
    new_film.release = release
    new_film.cast = cast
    new_film.director = director
    new_film.age_rating = age_rating
    new_film.save()

    return new_film

def make_film():
    return add_film("1234", "Test Film", "2002-09-02", "Bob Odenkirk", "Edgar Wright", "12")

class FilmTests(TestCase):

    def test_film_exists(self):
        make_film()
        self.assertTrue(Film.objects.filter(IMDB_num="1234").exists())

    def test_correct_slug(self):
        make_film()
        self.assertTrue(Film.objects.get(IMDB_num="1234").slug == "1234")

    def test_default_image(self):
        make_film()
        self.assertTrue(Film.objects.get(IMDB_num="1234").photo == "static/images/film_images/default.jpg")


def add_review(user, IMDB_num, stars, review_text):
    new_review = Review()
    new_review.user = user
    new_review.IMDB_num = IMDB_num
    new_review.stars = stars
    new_review.review_text = review_text
    new_review.save()

    return new_review

def make_review():
    return add_review(make_user_john(), make_film(), 5, "Very good")

class ReviewTests(TestCase):

    def test_review_exists(self):
        make_review()
        self.assertTrue(Review.objects.filter(IMDB_num="1234", stars=5, review_text="Very good").exists())
    
    def test_likes_zero(self):
        make_review()
        self.assertTrue(Review.objects.get(IMDB_num="1234", stars=5, review_text="Very good").likes == 0 
                        and Review.objects.get(IMDB_num="1234", stars=5, review_text="Very good").liked == "")
