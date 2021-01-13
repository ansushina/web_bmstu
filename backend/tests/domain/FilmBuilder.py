from modules.entities.Film import Film


class FilmMother:
    @staticmethod
    def one():
        film = FilmBuilder()
        film.title = 'film1'
        return film

    @staticmethod
    def two():
        film = FilmBuilder()
        film.title = 'film2'
        return film


class FilmBuilder:
    def __init__(self):
        self.id = None
        self.title = ""
        self.description = ""
        self.year = 0
        self.rating = 0
        self.genres = []
        self.actors = []
        self.countries = []
        self.image = None
        self.created = None

    def build(self):
        return Film(title=self.title,
                    year=self.year,
                    description=self.description,
                    genres=[],
                    actors=[],
                    countries=[],
                    )
