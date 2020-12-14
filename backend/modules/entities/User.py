class User:
    def __init__(self, username=None, email=None, password=None, created=None, avatar=None, id=None):
        self.username = username or ""
        self.password = password
        self.email = email or ""
        self.created = created
        self.avatar = avatar or ""
        self.id = id

