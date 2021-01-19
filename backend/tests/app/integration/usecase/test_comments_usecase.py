from pytest_mock import mocker

from modules.DBRepo.CommentDBRepo import CommentDBRepo
from modules.entities.Comment import Comment
from modules.usecases.CommentUsecases import CommentUsecases
from tests.domain.CommentBuilder import CommentMother


class TestCommentsUsecase:
    def test_get_one_success(self, simple_comment):
        # arrange
        usecase = CommentUsecases(CommentDBRepo())
        test_id = simple_comment.id
        expected_comment = simple_comment

        # act
        result_comments = usecase.get_comment(test_id)

        # assert
        assert result_comments.text == expected_comment.text

    def test_get_one_no_result(self):
        usecase = CommentUsecases(CommentDBRepo())

        result_comments = usecase.get_comment(1)
        assert result_comments is None

    def test_get_one_wrong_params(self):
        usecase = CommentUsecases(CommentDBRepo())

        result_comments = usecase.get_comment(-100)
        assert result_comments is None
