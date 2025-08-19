from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

def home(request):
    return render(request, "myapp/home.html")

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, "myapp/movie_list.html", {"movies": movies})

def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("movie_list")
    else:
        form = MovieForm()
    return render(request, "myapp/movie_form.html", {"form": form})
