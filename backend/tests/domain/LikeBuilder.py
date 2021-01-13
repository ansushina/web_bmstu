from modules.entities.Like import Like


class LikeMother:
    @staticmethod
    def one():
        like = LikeBuilder()
        like.value = 3
        return like

    @staticmethod
    def two():
        like = LikeBuilder()
        like.value = 2
        return like


class LikeBuilder:
    def __init__(self):
        self.value = 0
        self.author = 1
        self.film = 1
        self.id = id

    def build(self):
        return Like(value=self.value,
                    id=self.id,
                    author=self.author,
                    film=self.film,
        )