import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinema_project.settings')
import django

django.setup()
from django.contrib.auth.models import User
from django.utils import timezone
from random import randrange
from datetime import datetime
from cinema.models import Booking, Screen, Screening, Film, Review


def populate():
    try:
        user1 = User.objects.get(username='user1')
        user1.delete()
        user2 = User.objects.get(username='user2')
        user2.delete()
    except:
        pass

    # create 20 users
    users = []
    for i in range(20):
        users.append(User.objects.create_user("user"+str(i), password="user"+str(i)))

    films = []
    with open("films.tsv") as f:
        while line := f.readline():
            line = line.split("\t")
            if len(line) < 9:
                continue
            films.append(Film.objects.get_or_create(IMDB_num=line[0], title=line[2], release=datetime.strptime(line[5] + "-01-01", "%Y-%m-%d").date(), cast="Nicolas Cage, Pedro Pascal", director="Quentin Tarantino", age_rating="18"))


    # film1 = Film.objects.get_or_create(IMDB_num='tt0000001', title='Film 1', release=timezone.now().date(),
    #                                    cast='Actor 1, Actor 2', director='Director 1')
    # film2 = Film.objects.get_or_create(IMDB_num='tt0000002', title='Film 2', release=timezone.now().date(),
    #                                    cast='Actor 3, Actor 4', director='Director 2')
    # film3 = Film.objects.get_or_create(IMDB_num='tt0000003', title='Film 3', release=timezone.now().date(),
    #                                    cast='Actor 5, Actor 6', director='Director 3')

    reviews = []
    possible_comments = ["bad", "decent but i didnt like the end", "good"]
    for film in films:
        for i in range(10):
            user = users[randrange(0, len(users)-1)]
            review_text = possible_comments[randrange(0, len(possible_comments)-1)]
            likes = randrange(0, 1000)
            dislikes = randrange(0, 1000)
            reviews.append(Review.objects.get_or_create(user=user, IMDB_num=film[0], stars=randrange(1, 5), review_text=review_text, likes=likes, dislikes=dislikes))


if __name__ == '__main__':
    print('Starting Cinema population script...')
    populate()
