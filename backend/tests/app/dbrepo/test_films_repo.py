from modules.DBRepo.FilmDBRepo import FilmDBRepo


class TestFilmsRepo:
    def test_get_success(self, simple_film):
        # arrange
        expected_film = FilmDBRepo.decode_orm_film(simple_film)
        test_id = simple_film.id

        # act
        result_film = FilmDBRepo.get(film_id=test_id)

        # assert
        assert result_film.title == expected_film.title

    def test_get_fail_not_found(self):
        # arrange
        test_id = 1

        # act
        result_film = FilmDBRepo.get(film_id=test_id)

        # assert
        assert result_film is None

    def test_get_fail_not_normal(self):
        # arrange
        test_id = -100

        # act
        result_film = FilmDBRepo.get(film_id=test_id)

        # assert
        assert result_film is None

    def test_get_all_success(self, films_20):
        # arrange
        test_params = {}
        expected_films = []
        for g in films_20:
            expected_films.append(FilmDBRepo.decode_orm_film(g))
        expected_len = 10

        # act
        result_films = FilmDBRepo.get_all(test_params)

        # assert
        for i in range(expected_len):
            assert result_films[i].title == expected_films[i].title

    def test_get_all_no_results(self):
        # arrange
        test_params = {}
        expected_films = []

        # act
        result_films = FilmDBRepo.get_all(test_params)

        # assert
        assert result_films == expected_films

    def test_get_all_sort(self, films_3, films_3_core):
        # arrange
        test_params = {'sort': 'title'}
        expected_films = films_3_core
        expected_len = 3

        # act
        result_films = FilmDBRepo.get_all(test_params)

        # assert
        for i in range(expected_len):
            assert result_films[i].title == expected_films[i].title

    def test_get_all_genres_sort(self, films_3):
        # arrange
        expected_genre = films_3[0].genres.all()[0].id
        test_params = {'genre': [expected_genre]}
        expected_len = 3

        # act
        result_films = FilmDBRepo.get_all(test_params)

        # assert
        for i in range(len(result_films)):
            assert expected_genre in [result_films[i].genres[j].id for j in range(len(result_films[i].genres))]
