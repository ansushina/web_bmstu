from typing import List

from modules.entities.Comment import Comment
from tests.domain.CommentBuilder import CommentMother


class CommentDBRepoMock:

    @staticmethod
    def get(comment_id) -> Comment:
        return CommentMother.one().build()

    @staticmethod
    def get_all(film_id, o, l) -> List[Comment]:
        return [CommentMother.one().build(), CommentMother.two().build()]
