from typing import List

from modules.entities.Like import Like
from tests.domain.LikeBuilder import LikeMother


class LikeDBRepoMock:

    @staticmethod
    def get(like_id) -> Like:
        return LikeMother.one().build()

    @staticmethod
    def get_all(film_id) -> List[Like]:
        return [LikeMother.one().build(), LikeMother.two().build()]
