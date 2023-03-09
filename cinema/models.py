from django.db import models

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.template.defaultfilters import slugify


class Booking(models.Model):
    ticket_num = models.AutoField(primary_key=True)
    screen = models.ForeignKey('Screen', on_delete=models.CASCADE)
    seats = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"Booking: {self.ticket_num} - Screen: {self.screen} - Seats: {self.seats} - {self.date} at {self.time}"


class Screen(models.Model):
    screen_num = models.AutoField(primary_key=True)

    def __str__(self):
        return f"Screen: {self.screen_num}"


class Screening(models.Model):
    screen_num = models.ForeignKey('Screen', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"Screen: {self.screen_num} - {self.date} at {self.time}"


class Film(models.Model):
    IMDB_num = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255)
    release = models.DateField()
    cast = models.TextField()
    director = models.CharField(max_length=255)
    age_rating = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='static/images/film_images', blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.IMDB_num)
        super(Film, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    IMDB_num = models.ForeignKey('Film', on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_text = models.TextField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()

    def __str__(self):
        return f"{self.user} reviewed {self.IMDB_num}"
