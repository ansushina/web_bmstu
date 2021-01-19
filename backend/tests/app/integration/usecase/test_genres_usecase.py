from pytest_mock import mocker

from modules.DBRepo.GenreDBRepo import GenreDBRepo
from modules.entities.Genre import Genre
from modules.usecases.GenreUsecases import GenreUsecases
from tests.domain.GenreBuilder import GenreMother


class TestGenresUsecase:
    def test_get_one_success(self, simple_genre):
        # arrange
        usecase = GenreUsecases(GenreDBRepo())
        test_id = simple_genre.id
        expected_genre = simple_genre

        # act
        result_genres = usecase.get_genre(test_id)

        # assert
        assert result_genres.name == expected_genre.name

    def test_get_one_no_result(self):
        usecase = GenreUsecases(GenreDBRepo())

        result_genres = usecase.get_genre(1)
        assert result_genres is None

    def test_get_one_wrong_params(self):
        usecase = GenreUsecases(GenreDBRepo())

        result_genres = usecase.get_genre(-100)
        assert result_genres is None
