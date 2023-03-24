from django.contrib.auth.models import User


from cinema.models import Film, Review
from django.urls import reverse
from django.test import TestCase
from datetime import datetime, timedelta
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By


def add_user(username, email, password):
    new_user = User()

    new_user.username = username
    new_user.email = email
    new_user.password = password
    new_user.save()

    return new_user

def make_user_john():
    return add_user("JohnDaGoat12", "johnnyb2003@gmail.com", "John12345")


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



def make_film():
    return add_film("1234", "Test Film", "2002-09-02", "Bob Odenkirk", "Edgar Wright", "12")

def add_film(IMDB_num, title, release, cast, director, age_rating):

    new_film = Film(IMDB_num=IMDB_num, title=title, release=release,
                    cast=cast, director=director, age_rating=age_rating)
    new_film.save()

    return new_film
    
def make_film_goldfinger():
    return add_film(123456789, "Goldfinger", datetime.strptime("1964-09-17", "%Y-%m-%d").date(),
             "Sean Connery", "Guy Hamilton", "PG")

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

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_no_filter(self):
        num = 0
        film_names = ["the", "the a", "the b", "b the", "c the c"]
        for fn in film_names:
            Film.objects.get_or_create(IMDB_num=num, title=fn, release=datetime.now() - timedelta(days=365*(10-num)), cast="shdfisidf", director="ufh", age_rating="sfih")
            num += 1

            print(datetime.now() - timedelta(days=365*(10-num)))

        self.selenium.get(str(self.live_server_url) + '/cinema/search/?search=the')
        films = self.selenium.find_element(By.CSS_SELECTOR, "#films")  
        films = films.find_elements(By.TAG_NAME, "a")

        for f, fn in zip(films, film_names):
            self.assertEqual(f.text, fn)

    def test_review_exists(self):
        make_review()
        self.assertTrue(Review.objects.filter(IMDB_num="1234", stars=5, review_text="Very good").exists())
    
    def test_likes_zero(self):
        make_review()
        self.assertTrue(Review.objects.get(IMDB_num="1234", stars=5, review_text="Very good").likes == 0 
                        and Review.objects.get(IMDB_num="1234", stars=5, review_text="Very good").liked == "")
