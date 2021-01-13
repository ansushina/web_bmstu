from modules.DBRepo.GenreDBRepo import GenreDBRepo


class TestGenresRepo:
    def test_get_success(self, simple_genre):
        # arrange
        expected_genre = GenreDBRepo.decode_orm_genre(simple_genre)
        test_id = simple_genre.id

        # act
        result_genre = GenreDBRepo.get(genre_id=test_id)

        # assert
        assert result_genre.name == expected_genre.name

    def test_get_fail_not_found(self):
        # arrange
        test_id = 1

        # act
        result_genre = GenreDBRepo.get(genre_id=test_id)

        # assert
        assert result_genre is None

    def test_get_fail_not_normal(self):
        # arrange
        test_id = -100

        # act
        result_genre = GenreDBRepo.get(genre_id=test_id)

        # assert
        assert result_genre is None

    def test_get_all_success(self, genres_20):
        # arrange
        expected_genres = []
        for g in genres_20:
            expected_genres.append(GenreDBRepo.decode_orm_genre(g))

        # act
        result_genres = GenreDBRepo.get_all()

        # assert
        for i in range(len(expected_genres)):
            assert result_genres[i].name == expected_genres[i].name

    def test_get_all_no_results(self):
        # arrange
        expected_genres = []

        # act
        result_genres = GenreDBRepo.get_all()

        # assert
        assert result_genres == expected_genres
