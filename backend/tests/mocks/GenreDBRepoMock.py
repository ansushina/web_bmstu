from typing import List

from modules.entities.Genre import Genre
from tests.domain.GenreBuilder import GenreMother


class GenreDBRepoMock:

    @staticmethod
    def get(genre_id) -> Genre:
        return GenreMother.one().build()

    @staticmethod
    def get_all() -> List[Genre]:
        return [GenreMother.one().build(), GenreMother.two().build()]
