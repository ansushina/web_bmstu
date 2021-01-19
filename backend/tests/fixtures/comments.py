from random import choice, randint, sample

import pytest

from app.models.Actor import ActorORM
from app.models.Comment import CommentORM
from app.models.Country import CountryORM
from app.models.Film import FilmORM
from app.models.Genre import GenreORM
from .actors import *


@pytest.fixture
def simple_comment(simple_profile):
    f = FilmORM.objects.create(
        title='title',
        year=1930,
        description='blabla'
    )
    return CommentORM.objects.create(
        author_id=simple_profile.id,
        film_id=f.id,
        text="blabla"
    )


@pytest.fixture
def comments_20(simple_profile, genres_20, actors_20, countries_20):
    f = FilmORM.objects.create(
        title='title',
        year=1930,
        description='blabla'
    )
    comments = [CommentORM.objects.create(
        author_id=simple_profile.id,
        film_id=f.id,
        text=("blabla" + str(i))
    ) for i in range(20)]
    return comments
