from django.test import TestCase

from modules.DBRepo.GenreDBRepo import GenreDBRepo
from modules.entities.Genre import Genre


class TestGenreDBRepo(TestCase):
    fixtures = ['test_data.json']

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_get_one(self):
        # Arrange
        pk = 1
        expect = Genre(name="драма", id=pk)
        repo = GenreDBRepo()

        # Act
        result = repo.get(pk)

        print(result.name)

        # Assert
        self.assertTrue(expect.name == result.name and
                        expect.id == result.id)

    def test_get_all(self):
        # Arrange
        pk = 1
        genreslist = ["драма", "мелодрама", "криминал", "детектив", "приключения", "фантастика", "боевик", "биография",
                      "комедия", "семейный", "музыка", "военный",  "история", "фэнтези", "триллер",
                      "вестерн", "мультфильм", "спорт", "аниме", "мюзикл", "ужасы", "фильм-нуар"]
        expect = Genre(name="драма", id=pk)
        repo = GenreDBRepo()

        # Act
        result = repo.get(pk)

        print(result.name)

        # Assert
        self.assertTrue(expect.name == result.name and
                        expect.id == result.id)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)