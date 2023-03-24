from django.contrib.auth.models import User
from cinema.models import Film

from django.test import TestCase
from django.urls import reverse
from datetime import datetime, timedelta
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By

# Create your tests here.
def add_user(username, email, password):
    new_user = User()
    new_user.username = username
    new_user.email = email
    new_user.password = password
    new_user.save()

    return new_user


def sanitise(string):
    out = ""

    for c in string:
        if str(c).isalnum() or c == " ":
            out += str(c)

    return out

def make_user_john():
    add_user("JohnDaGoat12", "johnnyb2003@gmail.com", "John12345")


class UserTests(TestCase):

    def test_user_exists(self):
        make_user_john()
        self.assertTrue(User.objects.filter(username="JohnDaGoat12").exists())

    # def test_user_redirected(self):
    #     response = self.client.get(reverse("cinema:manager"))
    #     self.assertEquals(response.status_code, 302)

class MySeleniumTests(StaticLiveServerTestCase):
    #fixtures = ['user-data.json']

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
