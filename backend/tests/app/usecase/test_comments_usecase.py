from pytest_mock import mocker

from modules.DBRepo.CommentDBRepo import CommentDBRepo
from modules.entities.Comment import Comment
from modules.usecases.CommentUsecases import CommentUsecases
from tests.domain.CommentBuilder import CommentMother


class TestCommentsUsecase:
    def test_get_success(self, mocker):
        # arrange
        expected_comments = [CommentMother.one().build(), CommentMother.two().build()]
        mocker.patch('modules.DBRepo.CommentDBRepo.CommentDBRepo.get_all', return_value=expected_comments)
        usecase = CommentUsecases(CommentDBRepo())
        film_id = 1

        # act
        result_comments = usecase.get_all_comments(film_id, 0, len(expected_comments))

        # assert
        for i in range(len(expected_comments)):
            assert result_comments[i].text == expected_comments[i].text

    def test_get_one_success(self, simple_comment):
        # arrange
        usecase = CommentUsecases(CommentDBRepo())
        test_id = simple_comment.id
        expected_comment = simple_comment

        # act
        result_comments = usecase.get_comment(test_id)

        # assert
        assert result_comments.text == expected_comment.text

    def test_get_one_success_london(self, mocker):
        # arrange
        usecase = CommentUsecases(CommentDBRepo())
        test_id = 1
        expected_comment = CommentMother.one().build()
        mocker.patch('modules.DBRepo.CommentDBRepo.CommentDBRepo.get', return_value=expected_comment)

        # act
        result_comments = usecase.get_comment(test_id)

        # assert
        assert result_comments.text == expected_comment.text