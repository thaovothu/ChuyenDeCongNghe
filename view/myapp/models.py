from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    release_year = models.IntegerField()
    actors = models.ManyToManyField(Actor)

    def __str__(self):
        return self.title
