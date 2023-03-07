from django.urls import path
from cinema import views

app_name = 'cinema'

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.user, name='user'),
    path('manager/', views.manager, name='manager'),
    path('bookings/', views.bookings, name='bookings'),
    path('screenings/', views.screenings, name='screenings'),
    path('reviews/', views.reviews, name='reviews'),
    path('search/', views.search, name='search'),
    path('snacks/', views.snacks, name='snacks'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login')
]
