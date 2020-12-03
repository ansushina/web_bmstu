from modules.entities.User import User


class UserUsecases:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def get_user(self, username) -> (User, str):
        user, error = self.user_repo.get(username)
        return user, error

    def create_user(self, user_data) -> (User, str):
        user = User(username=user_data['username'],
                    password=user_data['password'],
                    email=user_data['email'])
        return self.user_repo.create(user)

    def create_session(self, user_data) -> (User, str):
        user = User(username=user_data['username'],
                    password=user_data['password'])
        return self.user_repo.create_session(user)

    def update_user(self, user_data) -> (User, str):
        user = User(username=user_data['username'],
                    email=user_data['email'],
                    id=user_data['id'],
                    avatar=user_data["avatar"])
        return self.user_repo.update(user)
