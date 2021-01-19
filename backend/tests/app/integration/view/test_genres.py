from django.http import HttpRequest

from app.views.GenreView import GenreView
from app.views.GenresListView import GenresListView
from modules.DBRepo.GenreDBRepo import GenreDBRepo
from modules.entities.Genre import Genre
from tests.domain.GenreBuilder import GenreMother


def genreToDict(genre: Genre):
    return {
        'name': genre.name,
        'id': genre.id
    }


class TestGenreView:
    def test_get_mock(self, client, mocker):
        # arrange
        test_genre = GenreMother.one().build()
        test_id = 1
        mocker.patch('modules.DBRepo.GenreDBRepo.GenreDBRepo.get', return_value=test_genre)
        view = GenreView()

        # act
        resp = view.get(HttpRequest(), test_id)

        # assert
        assert genreToDict(test_genre) == resp.data

    def test_all_mock(self, client, mocker):
        # arrange
        test_genres = [GenreMother.one().build(), GenreMother.two().build()]
        mocker.patch('modules.DBRepo.GenreDBRepo.GenreDBRepo.get_all', return_value=test_genres)
        expected_resp = [genreToDict(test_genres[i]) for i in range(len(test_genres))]
        view = GenresListView()

        # act
        resp = view.get(HttpRequest())

        # assert
        assert expected_resp == resp.data

    # def test_get_genre(self, simple_genre, client):
    #     # arrange
    #     test_genre = GenreDBRepo.decode_orm_genre(simple_genre)
    #
    #     # act
    #     resp = client.get("/api/v1/genres/" + str(test_genre.id) + "/")
    #
    #     # assert
    #     assert genreToDict(test_genre) == resp.json()
    #
    # def test_get_all_genres(self, genres_20, client):
    #     # arrange
    #     test_genres = [GenreDBRepo.decode_orm_genre(genres_20[i]) for i in range(len(genres_20))]
    #     expected_resp = [genreToDict(test_genres[i]) for i in range(len(test_genres))]
    #
    #     # act
    #     resp = client.get("/api/v1/genres/")
    #
    #     # assert
    #     assert expected_resp == resp.json()
