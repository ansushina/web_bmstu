import pytest

from app.models.Genre import GenreORM


@pytest.fixture
def simple_genre():
    return GenreORM.objects.create(
        name="романтика"
    )


@pytest.fixture
def genres_20():
    genres = [GenreORM.objects.create(name=("genre" + str(i))) for i in range(20)]
    return genres


