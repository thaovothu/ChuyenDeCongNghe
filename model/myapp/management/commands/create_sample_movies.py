from django.core.management.base import BaseCommand
from myapp.models import Actor, Movie
from datetime import date

class Command(BaseCommand):
    help = "Create sample actors and movies"

    def handle(self, *args, **options):
        Actor.objects.all().delete()
        Movie.objects.all().delete()

        # Actors
        actors_data = [
            {"name": "Leonardo DiCaprio", "birth_date": date(1974, 11, 11)},
            {"name": "Kate Winslet", "birth_date": date(1975, 10, 5)},
            {"name": "Tom Hanks", "birth_date": date(1956, 7, 9)},
        ]
        actors = [Actor.objects.create(**a) for a in actors_data]

        # Movies
        movie1 = Movie.objects.create(title="Titanic", release_date=date(1997, 12, 19), duration_minutes=195)
        movie1.actors.add(actors[0], actors[1])

        movie2 = Movie.objects.create(title="Catch Me If You Can", release_date=date(2002, 12, 25), duration_minutes=141)
        movie2.actors.add(actors[0], actors[2])

        self.stdout.write(self.style.SUCCESS("Sample movies and actors created!"))
