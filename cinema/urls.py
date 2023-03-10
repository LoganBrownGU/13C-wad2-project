from django.urls import path
from cinema import views

app_name = 'cinema'

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.user, name='user'),
    path('manager/', views.manager, name='manager'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('reviews/<slug:film_title_slug>/', views.reviews, name='reviews'),

]
