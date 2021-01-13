from modules.DBRepo.FilmDBRepo import FilmDBRepo
from modules.usecases.FilmUsecases import FilmUsecases

from pytest_mock import mocker

from tests.domain.FilmBuilder import FilmMother


class TestFilmsUsecase:
    def test_get_success(self, simple_film):
        # arrange
        usecase = FilmUsecases(FilmDBRepo())
        test_id = simple_film.id
        expected_film = simple_film

        # act
        result_films = usecase.get_film(test_id)

        # assert
        assert result_films.title == expected_film.title

    def test_get_success_london(self, mocker):
        # arrange
        test_id = 1
        expected_film = FilmMother.one().build()
        mocker.patch('modules.DBRepo.FilmDBRepo.FilmDBRepo.get', return_value=expected_film)
        usecase = FilmUsecases(FilmDBRepo())

        # act
        result_films = usecase.get_film(test_id)

        # assert
        assert result_films.title == expected_film.title

    # def test_get_one_no_result(self):
    #     usecase = FilmUsecases(FilmDBRepo())
    #
    #     result_films = usecase.get_film(1)
    #     assert result_films is None
    #
    # def test_get_one_wrong_params(self):
    #     usecase = FilmUsecases(FilmDBRepo())
    #
    #     result_films = usecase.get_film(-100)
    #     assert result_films is None

    def test_get_all_success(self, mocker):
        # arrange
        expected_films = [FilmMother.one().build(), FilmMother.two().build()]
        mocker.patch('modules.DBRepo.FilmDBRepo.FilmDBRepo.get_all', return_value=expected_films)
        usecase = FilmUsecases(FilmDBRepo())
        test_params = {}

        # act
        result_genres = usecase.get_all_films(test_params)

        # assert
        for i in range(len(expected_films)):
            assert result_genres[i].title == expected_films[i].title
