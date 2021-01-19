from modules.DBRepo.GenreDBRepo import GenreDBRepo
from modules.usecases.GenreUsecases import GenreUsecases
from tests.domain.GenreBuilder import GenreMother
from tests.mocks.GenreDBRepoMock import GenreDBRepoMock


class TestGenresUsecase:
    def test_get_success(self, mocker):
        # arrange
        expected_genres = [GenreMother.one().build(), GenreMother.two().build()]
        mocker.patch('modules.DBRepo.GenreDBRepo.GenreDBRepo.get_all', return_value=expected_genres)
        usecase = GenreUsecases(GenreDBRepo())

        # act
        result_genres = usecase.get_all_genres()

        # assert
        for i in range(len(expected_genres)):
            assert result_genres[i].name == expected_genres[i].name

    def test_get_one_success_london(self, mocker):
        # arrange
        usecase = GenreUsecases(GenreDBRepo())
        test_id = 1
        expected_genre = GenreMother.one().build()
        mocker.patch('modules.DBRepo.GenreDBRepo.GenreDBRepo.get', return_value=expected_genre)

        # act
        result_genres = usecase.get_genre(test_id)

        # assert
        assert result_genres.name == expected_genre.name

    def test_get_one_my_mock(self):
        # arrange
        usecase = GenreUsecases(GenreDBRepoMock())
        test_id = 1
        expected_genre = GenreMother.one().build()

        # act
        result_genres = usecase.get_genre(test_id)

        # assert
        assert result_genres.name == expected_genre.name

    def test_get_all_my_mock(self):
        # arrange
        expected_genres = [GenreMother.one().build(), GenreMother.two().build()]
        usecase = GenreUsecases(GenreDBRepoMock())

        # act
        result_genres = usecase.get_all_genres()

        # assert
        for i in range(len(expected_genres)):
            assert result_genres[i].name == expected_genres[i].name
