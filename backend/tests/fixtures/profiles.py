

import pytest
from django.contrib.auth.models import User as UserORM
from memory_profiler import profile

from app.models.Profile import ProfileORM

from modules.entities.User import User

@pytest.fixture
def simple_profile():
    orm_user = UserORM.objects.create_user(username="vasya", email="vasya@mail.ru", password="1111")
    return ProfileORM.objects.create(
        user=orm_user
    )


@pytest.fixture
def simple_profile_user():
    return User(
        username="vasya",
        email="vasya@mail.ru",
        password="1111")
