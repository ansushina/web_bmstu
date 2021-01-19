from typing import List

from modules.entities.Film import Film
from tests.domain.FilmBuilder import FilmMother


class FilmDBRepoMock:

    @staticmethod
    def get(film_id) -> Film:
        return FilmMother.one().build()

    @staticmethod
    def get_all(params) -> List[Film]:
        return [FilmMother.one().build(), FilmMother.two().build()]
