from django.contrib import admin
from cinema.models import Booking, Screen, Screening, Film, Review

admin.site.register(Booking)
admin.site.register(Screen)
admin.site.register(Screening)
admin.site.register(Film)
admin.site.register(Review)
