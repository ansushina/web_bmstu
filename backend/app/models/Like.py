from django.contrib.auth.models import User
from django.db import models

from app.models.Film import FilmORM as Film
from app.models.Profile import ProfileORM as Profile


class LikeORM(models.Model):
    film = models.ForeignKey(
        to=Film,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE
    )

    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    # objects = LikeManageger()

    def __str__(self):
        return "from " + self.author.user.username + " on " + self.film.title