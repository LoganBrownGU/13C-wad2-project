from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

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
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user} reviewed {self.IMDB_num}"
