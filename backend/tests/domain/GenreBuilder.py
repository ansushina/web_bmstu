from modules.entities.Genre import Genre


class GenreMother:
    @staticmethod
    def one():
        genre = GenreBuilder()
        genre.name = 'genre1'
        return genre

    @staticmethod
    def two():
        genre = GenreBuilder()
        genre.name = 'genre2'
        return genre


class GenreBuilder:
    def __init__(self):
        self.name = ""
        self.id = 0

    def build(self):
        return Genre(name=self.name, id=self.id)