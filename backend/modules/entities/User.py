class User:
    def __init__(self, username, email=None, password=None, created=None, avatar=None, id=None):
        self.username = username
        self.password = password
        self.email = email
        self.created = created
        self.avatar = avatar
        self.id = id

