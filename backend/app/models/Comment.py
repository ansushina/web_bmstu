from django.db import models

from app.models.Film import FilmORM as Film
from app.models.Profile import ProfileORM as Profile


class CommentORM(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        to=Profile,
        on_delete=models.CASCADE
    )
    film = models.ForeignKey(
        to=Film,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text + " from " + self.author.user.username + " on " + self.film.title
