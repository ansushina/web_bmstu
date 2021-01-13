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

    def test_get_one_success_london(self, mocker):
        # arrange
        usecase = LikeUsecases(LikeDBRepo(), FilmDBRepo())
        test_id = 1
        expected_like = LikeMother.one().build()
        mocker.patch('modules.DBRepo.LikeDBRepo.LikeDBRepo.get', return_value=expected_like)

        # act
        result_likes = usecase.get_like(test_id)

        # assert
        assert result_likes.value == expected_like.value

    def test_create_like_mock(self, mocker):
        # arrange
        expected_like = LikeMother.one().build()
        user_id = expected_like.author
        film_id = expected_like.film
        value = expected_like.value
        usecase = LikeUsecases(LikeDBRepo(), FilmDBRepo())
        mocker.patch('modules.DBRepo.LikeDBRepo.LikeDBRepo.create', return_value=(expected_like, None))
        mocker.patch('modules.DBRepo.FilmDBRepo.FilmDBRepo.count_rating', return_value=None)

        # act
        (like, error) = usecase.create_like(user_id=user_id, film_id=film_id, value=value)

        # assert
        assert like.value == expected_like.value

    # def test_get_one_no_result(self):
    #     usecase = likeUsecases(likeDBRepo())
    #
    #     result_likes = usecase.get_like(1)
    #     assert result_likes is None
    #
    # def test_get_one_wrong_params(self):
    #     usecase = likeUsecases(likeDBRepo())
    #
    #     result_likes = usecase.get_like(-100)
    #     assert result_likes is None

