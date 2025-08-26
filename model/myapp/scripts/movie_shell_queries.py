from myapp.models import Actor, Movie
from django.db.models import Q


all_actors = Actor.objects.all()


all_movies = Movie.objects.all()


leo = Actor.objects.get(name="Leonardo DiCaprio")
leo_movies = leo.movies.all()


titanic = Movie.objects.get(title="Titanic")
actors_in_titanic = titanic.actors.all()


long_movies = Movie.objects.filter(duration_minutes__gt=150)


movies_without_leo = Movie.objects.exclude(actors__name="Leonardo DiCaprio")


catch_or_long_movies = Movie.objects.filter(
    Q(title__icontains="Catch") | Q(duration_minutes__gt=150)
)


actors_before_1970 = Actor.objects.filter(birth_date__year__lt=1970)


kate = Actor.objects.get(name="Kate Winslet")
kate_movies_count = kate.movies.count()


tom = Actor.objects.get(name="Tom Hanks")
first_movie_tom = tom.movies.first()


c_movies_long = Movie.objects.filter(
    Q(title__startswith="C") & Q(duration_minutes__gt=140)
)
