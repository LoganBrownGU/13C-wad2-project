import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinema_project.settings')
import django

django.setup()
from django.contrib.auth.models import User
from random import randrange
from datetime import datetime
from cinema.models import Film, Review


def sanitise(string):
    out = ""

    for c in string:
        if str(c).isalnum() or c == " ":
            out += str(c)

    return out

def generate_review():
    
    out = ""
    for i in range(20):
        out += chr(randrange(ord('a'), ord('z')))

    print(out)

    return out


def populate():
    users = []
    for i in range(20):
        users.append(User.objects.create_user("user" + str(i), password="user" + str(i)))

    films = []
    with open("films.tsv") as f:
        contents = f.readlines()
        for line in contents:
            line = line.split("\t")
            if len(line) < 9:
                continue

            line[2] = sanitise(line[2])

            films.append(Film.objects.get_or_create(IMDB_num=line[0], title=line[2],
                                                    release=datetime.strptime(line[5] + "-01-01", "%Y-%m-%d").date(),
                                                    cast="Nicolas Cage, Pedro Pascal", director="Quentin Tarantino",
                                                    age_rating="18"))

    reviews = []

    for film in films:
        for i in range(10):
            user = users[randrange(0, len(users))]
            review_text = generate_review() #possible_comments[randrange(0, len(possible_comments))]
            likes = randrange(0, 1000)
            reviews.append(Review.objects.get_or_create(user=user, IMDB_num=film[0], stars=randrange(1, 5),
                                                        review_text=review_text, likes=likes))


if __name__ == '__main__':
    print('Starting Cinema population script...')
    populate()
    print('Cinema population script finished.')
