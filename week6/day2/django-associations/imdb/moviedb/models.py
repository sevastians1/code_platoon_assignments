from django.db import models


class Movie(models.Model):
    pass


class Actor(models.Model):
    movies = models.ManyToManyField(Movie, related_name="actors", through="Role")


class Role(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name="roles")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="roles")

    class Meta:
        unique_together = (("movie", "actor"))
