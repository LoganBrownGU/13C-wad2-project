from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from cinema.forms import UserForm
from cinema.models import Film, Review


def home(request):
    film_list = Film.objects.order_by('-release')[:5]

    context_dict = {}
    context_dict['films'] = film_list

    return render(request, 'cinema/home.html', context=context_dict)


def user(request):
    context_dict = {}

    return render(request, 'cinema/user.html', context=context_dict)


def manager(request):
    context_dict = {}

    return render(request, 'cinema/manager.html', context=context_dict)


def bookings(request):
    context_dict = {}

    return render(request, 'cinema/bookings.html', context=context_dict)


def screenings(request):
    context_dict = {}

    return render(request, 'cinema/screenings.html', context=context_dict)


def reviews(request, film_title_slug):
    context_dict = {}
    try:
        film = Film.objects.get(slug=film_title_slug)
        reviews = Review.objects.filter(IMDB_num=film.IMDB_num).order_by('-likes')
        context_dict['reviews'] = reviews
        context_dict['film'] = film
    except Film.DoesNotExist:
        context_dict['film'] = None
        context_dict['reviews'] = None

    return render(request, 'cinema/reviews.html', context=context_dict)


def search(request):
    context_dict = {}

    return render(request, 'cinema/search.html', context=context_dict)


def snacks(request):
    context_dict = {}

    return render(request, 'cinema/snacks.html', context=context_dict)


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request,
                  'cinema/register.html',
                  context={'user_form': user_form,
                           'registered': registered})


def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('cinema:home'))
            else:
                return HttpResponse("Your Cinema account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'cinema/login.html')


def user_logout(request):
    logout(request)
    return redirect(reverse('cinema:home'))
