from modules.DBRepo.FilmDBRepo import FilmDBRepo
from modules.usecases.FilmUsecases import FilmUsecases

from pytest_mock import mocker

from tests.domain.FilmBuilder import FilmMother
from tests.mocks.FilmDBRepoMock import FilmDBRepoMock


class TestFilmsUsecase:

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

    def test_get_my_mock(self):
        # arrange
        test_id = 1
        expected_film = FilmMother.one().build()
        usecase = FilmUsecases(FilmDBRepoMock())

        # act
        result_films = usecase.get_film(test_id)

        # assert
        assert result_films.title == expected_film.title

    def test_get_all_success(self):
        # arrange
        expected_films = [FilmMother.one().build(), FilmMother.two().build()]
        usecase = FilmUsecases(FilmDBRepoMock())
        test_params = {}

        # act
        result_genres = usecase.get_all_films(test_params)

        # assert
        for i in range(len(expected_films)):
            assert result_genres[i].title == expected_films[i].title
