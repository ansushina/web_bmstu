from pytest_mock import mocker

from modules.DBRepo.FilmDBRepo import FilmDBRepo
from modules.DBRepo.LikeDBRepo import LikeDBRepo
from modules.entities.Like import Like
from modules.usecases.LikeUsecases import LikeUsecases
from tests.domain.LikeBuilder import LikeMother


class TestLikesUsecase:
    def test_get_one_success(self, simple_like):
        # arrange
        usecase = LikeUsecases(LikeDBRepo(), FilmDBRepo())
        test_id = simple_like.id
        expected_like = simple_like

        # act
        result_likes = usecase.get_like(test_id)

        # assert
        assert result_likes.value == expected_like.value

    def test_get_one_no_result(self):
        usecase = LikeUsecases(LikeDBRepo(), FilmDBRepo())

        result_likes = usecase.get_like(1)
        assert result_likes is None

    def test_get_one_wrong_params(self):
        usecase = LikeUsecases(LikeDBRepo(), FilmDBRepo())

        result_likes = usecase.get_like(-100)
        assert result_likes is None

