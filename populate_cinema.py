import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinema_project.settings')
import django

django.setup()
from django.contrib.auth.models import User
from django.utils import timezone
from cinema.models import Booking, Screen, Screening, Film, Review


def populate():
    try:
        user1 = User.objects.get(username='user1')
        user1.delete()
        user2 = User.objects.get(username='user2')
        user2.delete()
    except:
        pass
    user1 = User.objects.create_user('user1', password='password')
    user2 = User.objects.create_user('user2', password='password123')

    screen1 = Screen.objects.get_or_create(screen_num=1)
    screen2 = Screen.objects.get_or_create(screen_num=2)
    screen3 = Screen.objects.get_or_create(screen_num=3)

    screening1 = Screening.objects.get_or_create(screen_num=screen1[0], date=timezone.now().date(),
                                                 time=timezone.now().time())
    screening2 = Screening.objects.get_or_create(screen_num=screen2[0], date=timezone.now().date(),
                                                 time=timezone.now().time())
    screening3 = Screening.objects.get_or_create(screen_num=screen3[0], date=timezone.now().date(),
                                                 time=timezone.now().time())

    film1 = Film.objects.get_or_create(IMDB_num='tt0000001', title='Film 1', release=timezone.now().date(),
                                       cast='Actor 1, Actor 2', director='Director 1')
    film2 = Film.objects.get_or_create(IMDB_num='tt0000002', title='Film 2', release=timezone.now().date(),
                                       cast='Actor 3, Actor 4', director='Director 2')
    film3 = Film.objects.get_or_create(IMDB_num='tt0000003', title='Film 3', release=timezone.now().date(),
                                       cast='Actor 5, Actor 6', director='Director 3')

    booking1 = Booking.objects.get_or_create(screen=screen1[0], seats='A1,A2', date=timezone.now().date(),
                                             time=timezone.now().time())
    booking2 = Booking.objects.get_or_create(screen=screen2[0], seats='B1,B2', date=timezone.now().date(),
                                             time=timezone.now().time())
    booking3 = Booking.objects.get_or_create(screen=screen3[0], seats='C1,C2', date=timezone.now().date(),
                                             time=timezone.now().time())

    review1 = Review.objects.get_or_create(user=user1, IMDB_num=film1[0], stars=2, comments='Bad', likes=5)
    review2 = Review.objects.get_or_create(user=user1, IMDB_num=film2[0], stars=1, comments='Very Bad', likes=23)
    review3 = Review.objects.get_or_create(user=user2, IMDB_num=film3[0], stars=5, comments='Good', likes=135)


if __name__ == '__main__':
    print('Starting Cinema population script...')
    populate()
