from django.contrib import admin
from cinema.models import Film, Review


class FilmAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('IMDB_num',)}


admin.site.register(Film, FilmAdmin)
admin.site.register(Review)
