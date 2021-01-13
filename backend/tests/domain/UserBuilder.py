from modules.entities.User import User


class UserMother:
    @staticmethod
    def one():
        user = UserBuilder()
        user.username = 'user1'
        user.password = "1111"
        user.email = "vasya@gmail.com"
        return user

    def two(self):
        user = UserBuilder()
        user.username = 'user2'
        user.password = "1111"
        user.email = "vasya111@gmail.com"
        return user

    def without_name(self):
        user = UserBuilder()
        user.username = None
        user.password = "1111"
        user.email = "vasya@gmail.com"
        return user

    def without_email(self):
        user = UserBuilder()
        user.username = 'user1'
        user.password = "1111"
        return user

    def without_password(self):
        user = UserBuilder()
        user.username = 'user1'
        user.email = "vasya@gmail.com"
        return user


class UserBuilder:
    def __init__(self):
        self.username = ""
        self.password = None
        self.email = ""
        self.created = None
        self.avatar = ""
        self.id = None

    def build(self):
        return User(username=self.username,
                    password=self.password,
                    email=self.email,
                    created=self.created,
                    avatar=self.avatar,
                    id=self.id)
