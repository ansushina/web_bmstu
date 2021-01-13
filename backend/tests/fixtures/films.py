from random import choice, randint, sample

import pytest

from app.models.Actor import ActorORM
from app.models.Country import CountryORM
from app.models.Film import FilmORM
from app.models.Genre import GenreORM
from modules.entities.Film import Film


@pytest.fixture
def simple_film(genres_20, actors_20, countries_20):
    f = FilmORM.objects.create(
        title='title',
        year=1930,
        description='blabla'
    )
    return f


@pytest.fixture
def films_20(genres_20, actors_20, countries_20):
    films = []

    for i in range(20):
        f = FilmORM.objects.create(
            title='title',
            year=1930,
            description='blabla'
        )
        films.append(f)
    return films


@pytest.fixture
def films_3(genres_20, actors_20, countries_20):
    films = []
    f = FilmORM.objects.create(
        title='bbbbbb',
        year=1930,
        description='b'
    )
    gids = list(GenreORM.objects.values_list('id', flat=True))
    f.genres.add(gids[0])
    f.save()
    films.append(f)

    f = FilmORM.objects.create(
        title='cccccccc',
        year=1930,
        description='b'
    )
    gids = list(GenreORM.objects.values_list('id', flat=True))
    f.genres.add(gids[2])
    f.save()
    films.append(f)

    f = FilmORM.objects.create(
        title='aaaaaaaa',
        year=1930,
        description='b'
    )
    gids = list(GenreORM.objects.values_list('id', flat=True))
    f.genres.add(gids[1])
    f.save()
    films.append(f)
    return films


@pytest.fixture
def films_3_core():
    films = [Film(title=t,
                  description='',
                  genres=[],
                  actors=[],
                  countries=[],
                  year=1930) for t in ['aaaaaaaa',
                                       'bbbbbb',
                                       'cccccccc']]
    return films
