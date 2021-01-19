import pytest

from modules.DBRepo.UserDBRepo import UserDBRepo
from modules.entities.User import User
from modules.usecases.UserUsecases import UserUsecases
from tests.domain.UserBuilder import UserMother


def userToDict(user: User):
    return {
        'username': user.username,
        'email': user.email,
        'password': user.password or "",
    }


class TestUserUsecase:
    def test_create_user(self):
        # arrange
        userdata = userToDict(UserMother.one().build())
        usecase = UserUsecases(UserDBRepo())

        # act
        (user, error) = usecase.create_user(userdata)

        # assert
        assert error is None
        assert userdata['username'] == user.username
        assert userdata['email'] == user.email

    def test_create_user_duple_username(self):
        # arrange
        builder = UserMother.one()
        userdata_1 = userToDict(builder.build())

        builder.email = "sadad@dd.com"
        userdata_2 = userToDict(builder.build())

        usecase = UserUsecases(UserDBRepo())

        # act
        (user_1, error_1) = usecase.create_user(userdata_1)

        (user_2, error_2) = usecase.create_user(userdata_2)

        # assert
        assert error_2 == "invalid_username"

    def test_create_user_duple_email(self):
        # arrange
        builder = UserMother.one()
        userdata_1 = userToDict(builder.build())

        builder.name = "user122212"
        userdata_2 = userToDict(builder.build())

        usecase = UserUsecases(UserDBRepo())

        # act
        (user_1, error_1) = usecase.create_user(userdata_1)

        (user_2, error_2) = usecase.create_user(userdata_2)

        # assert
        assert error_2 == "invalid_email"

    def test_create_user_no_username(self):
        # arrange
        userdata = {
            'password': '1111',
            'email': 'vasya@gmail.com',
        }
        usecase = UserUsecases(UserDBRepo())

        with pytest.raises(KeyError) as r:
            # act
            (user, error) = usecase.create_user(userdata)

            # assert
            assert r

    def test_create_user_no_email(self):
        # arrange
        userdata = {
            'username': 'user1',
            'password': '1111',
        }
        usecase = UserUsecases(UserDBRepo())

        with pytest.raises(KeyError) as r:
            # act
            (user, error) = usecase.create_user(userdata)

            # assert
            assert r

    def test_create_user_no_password(self):
        # arrange
        userdata = {
            'username': 'user1',
            'email': 'vasya@gmail.com',
        }
        usecase = UserUsecases(UserDBRepo())

        with pytest.raises(KeyError) as r:
            # act
            (user, error) = usecase.create_user(userdata)

            # assert
            assert r