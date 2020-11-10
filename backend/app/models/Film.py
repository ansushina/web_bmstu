from django.db import models

from modules.managers.FilmManager import FilmManager
from app.models.Actor import Actor
from app.models.Country import Country
from app.models.Genre import Genre


class FilmORM(models.Model):
    year = models.IntegerField(default=0)
    title = models.TextField()
    description = models.TextField()
    rating = models.IntegerField(default=0)
    genres = models.ManyToManyField(
        to=Genre,
        blank=True)
    actors = models.ManyToManyField(
        to=Actor,
        blank=True
    )
    countries = models.ManyToManyField(
        to=Country,
        blank=True
    )

    image = models.ImageField(
        upload_to='films/%Y/%m/%d/', null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    objects = FilmManager()

    def __str__(self):
        return self.title

