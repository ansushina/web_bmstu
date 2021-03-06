import pytest

from app.models.Actor import ActorORM


@pytest.fixture
def simple_actor():
    return ActorORM.objects.create(
        firstName="Вася",
        lastName="Пупкин"
    )


@pytest.fixture
def actors_20():
    actors = [ActorORM.objects.create(firstName=("actor" + str(i)), lastName=("last" + str(i))) for i in range(20)]
    return actors


