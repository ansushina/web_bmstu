from modules.DBRepo.GenreDBRepo import GenreDBRepo
from modules.usecases.GenreUsecases import GenreUsecases


class GenreFactory:
    @staticmethod
    def get_genre_usecase() -> GenreUsecases:
        return GenreUsecases(GenreDBRepo())
