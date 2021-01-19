from typing import List

from modules.entities.User import User
from tests.domain.UserBuilder import UserMother


class UserDBRepoMock:

    @staticmethod
    def get(user_id) -> (User, str):
        return UserMother.one().build(), None
