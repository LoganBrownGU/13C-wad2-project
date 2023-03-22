import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse
from django.urls import reverse
from cinema.forms import UserForm, ReviewForm, FilmForm
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
    context_dict = {'film_added': False, 'film_form': FilmForm()}
    if request.method == 'POST':
        film_form = FilmForm(request.POST, request.FILES)
        if film_form.is_valid():
            film_form.save()
            context_dict['film_added'] = True
        else:
            context_dict['form_errors'] = film_form.errors

    return render(request, 'cinema/manager.html', context=context_dict)


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

def like(request, film_title_slug):
    try:
        review = Review.objects.get(review_text=request.POST.get("review_text"), IMDB_num=film_title_slug, stars=request.POST.get("stars"))
        review.likes += 1
        review.save()
        
    except Review.DoesNotExist:
        print(request.POST.get("review_text"), request.POST.get("imdb"), request.POST.get("stars"))
    except Review.MultipleObjectsReturned:
        reviews = Review.objects.filter(review_text=request.POST.get("review_text"), IMDB_num=film_title_slug, stars=request.POST.get("stars"))
        for review in reviews:
            review.likes += 1
            review.save()

    if request.POST.get("origin") == "reviews":
        return redirect(reverse('cinema:reviews', kwargs={'film_title_slug':film_title_slug}))
    
    elif request.POST.get("origin") == "user":
        return redirect(reverse('cinema:profile', kwargs={'username':request.POST.get("user")}))

def search(request):
    context_dict = {}
    if request.method != "GET":
        context_dict["films"] = None
        return render(request, 'cinema/search.html', context=context_dict)

    search_text = request.GET.get("search")
    context_dict["search"] = search_text

    films = Film.objects.filter(title__icontains=search_text)
    context_dict["films"] = films

    return render(request, 'cinema/search.html', context=context_dict)


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


def change_search_filter(request):
    if request.method != "GET":
        return HttpResponse(None)
    
    filter = request.GET.get("filter")
    search_text = request.GET.get("search")

    films = Film.objects.filter(title__icontains=search_text)

    if (filter == "recent"):
        films = films.order_by("-release")[:10]
        films = list(films)
    elif (filter == "popular"):

        def find_mean(f):
            reviews = Review.objects.filter(IMDB_num=f.IMDB_num)
            mean = 0
                
            for review in reviews:
                mean += review.stars
                
            mean /= len(reviews)
            return mean
            
        films = sorted(films, key=lambda f: find_mean(f), reverse=True)[:10]

    outstr = "<xml>"
    for film in films:
        outstr += "<film><title>" + film.title + "</title><director>" + film.director + "</director><release>" + str(film.release) + "</release>" + "<slug>" + film.slug + "</slug></film>\n"
    outstr += "</xml>"

    return HttpResponse(outstr)


def leave_review(request, film_title_slug):
    try:
        film = Film.objects.get(slug=film_title_slug)
    except Film.DoesNotExist:
        film = None

    if film is None:
        return redirect('/cinema/')

    user = request.user

    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            if film:
                review = form.save(commit=False)
                review.IMDB_num = film
                review.user = user
                review.likes = 0
                review.dislikes = 0
                review.save()

                return redirect(reverse('cinema:reviews', kwargs={'film_title_slug': film_title_slug}))

        else:
            print(form.errors)

    context_dict = {'form': form, 'film': film, 'user': user}
    return render(request, 'cinema/leave_review.html', context=context_dict)


def user_profile(request, username):
    context = {}

    try:
        user = User.objects.get(username=username)
        context["profile"] = user
        context["reviews"] = Review.objects.filter(user=user).order_by("-likes")

    except:
        return redirect(reverse("cinema:home"))

    return render(request, "cinema/user.html", context=context)


def change_search_filter(request):
    if request.method == "GET":
        filter = request.GET.get("filter")
        search_text = request.GET.get("search")

        print("search: " + filter)

        films = Film.objects.filter(title__startswith=search_text)

        if (filter == "recent"):
            films = films.order_by("-release")[:10]
            films = list(films)
        elif (filter == "popular"):

            def find_mean(f):
                reviews = Review.objects.filter(IMDB_num=f.IMDB_num)
                mean = 0

                for review in reviews:
                    mean += review.stars

                mean /= len(reviews)
                return mean

            films = sorted(films, key=lambda f: find_mean(f), reverse=True)[:10]

        outstr = "<xml>"
        for film in films:
            outstr += "<film><title>" + film.title + "</title><director>" + film.director + "</director><release>" + str(
                film.release) + "</release>" + "<slug>" + film.slug + "</slug></film>\n"
        outstr += "</xml>"

        return HttpResponse(outstr)

    return HttpResponse(None)
