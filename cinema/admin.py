from django.contrib import admin
from cinema.models import Booking, Screen, Screening, Film, Review

class FilmAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('IMDB_num',)}

admin.site.register(Booking)
admin.site.register(Screen)
admin.site.register(Screening)
admin.site.register(Film, FilmAdmin)
admin.site.register(Review)