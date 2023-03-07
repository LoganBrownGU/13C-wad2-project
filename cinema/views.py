from django.shortcuts import render, redirect
from django.http import HttpResponse

from cinema.forms import UserForm


def home(request):
    context_dict = {}

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


def reviews(request):
    context_dict = {}

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
