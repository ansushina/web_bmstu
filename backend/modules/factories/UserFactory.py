from modules.DBRepo.UserDBRepo import UserDBRepo
from modules.usecases.UserUsecases import UserUsecases


class UserFactory:
    @staticmethod
    def get_user_usecase() -> UserUsecases:
        return UserUsecases(UserDBRepo())
