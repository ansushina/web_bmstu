import pytest

from app.models.Film import FilmORM
from app.models.Like import LikeORM


@pytest.fixture
def simple_like(simple_profile, genres_20, actors_20, countries_20):
    f = FilmORM.objects.create(
        title='title',
        year=1930,
        description='blabla'
    )
    return LikeORM.objects.create(
        author_id=simple_profile.id,
        film_id=f.id,
        value=1
    )


@pytest.fixture
def likes_20(simple_profile, genres_20, actors_20, countries_20):
    f = FilmORM.objects.create(
        title='title',
        year=1930,
        description='blabla'
    )
    likes = [LikeORM(
        author_id=simple_profile.id,
        film_id=f.id,
        value=(i % 20)
    ) for i in range(20)]
    return LikeORM.objects.bulk_create(likes)
