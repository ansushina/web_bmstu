from modules.DBRepo.FilmDBRepo import FilmDBRepo
from modules.usecases.FilmUsecases import FilmUsecases


class FilmFactory:
    @staticmethod
    def get_film_usecase() -> FilmUsecases:
        return FilmUsecases(FilmDBRepo())