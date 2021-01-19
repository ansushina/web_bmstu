import pytest

from modules.DBRepo.UserDBRepo import UserDBRepo
from modules.entities.User import User
from modules.usecases.UserUsecases import UserUsecases
from tests.domain.UserBuilder import UserMother
from tests.mocks.UserDBRepoMock import UserDBRepoMock


def userToDict(user: User):
    return {
        'username': user.username,
        'email': user.email,
        'password': user.password or "",
    }


class TestUserUsecase:
    def test_create_user_mock(self, mocker):
        # arrange
        userdata = userToDict(UserMother.one().build())
        usecase = UserUsecases(UserDBRepo())
        mocker.patch('modules.DBRepo.UserDBRepo.UserDBRepo.create', return_value=(UserMother.one().build(), None))

        # act
        (user, error) = usecase.create_user(userdata)

        # assert
        assert error is None
        assert userdata['username'] == user.username
        assert userdata['email'] == user.email

    def test_get_one_success_london(self, mocker):
        # arrange
        usecase = UserUsecases(UserDBRepo())
        test_id = 1
        expected_user = UserMother.one().build()
        mocker.patch('modules.DBRepo.UserDBRepo.UserDBRepo.get', return_value=(expected_user, None))

        # act
        (result_users, error) = usecase.get_user(test_id)

        # assert
        assert result_users.username == expected_user.username

    def test_get_one_my_mock(self):
        # arrange
        usecase = UserUsecases(UserDBRepoMock())
        test_id = 1
        expected_user = UserMother.one().build()

        # act
        (result_users, error) = usecase.get_user(test_id)

        # assert
        assert result_users.username == expected_user.username