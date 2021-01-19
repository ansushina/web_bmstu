from pytest_mock import mocker

from modules.DBRepo.CountryDBRepo import CountryDBRepo
from modules.entities.Country import Country
from modules.usecases.CountryUsecases import CountryUsecases
from tests.domain.CountryBuilder import CountryMother


class TestCountriesUsecase:
    def test_get_one_success(self, simple_country):
        # arrange
        usecase = CountryUsecases(CountryDBRepo())
        test_id = simple_country.id
        expected_country = simple_country

        # act
        result_countries = usecase.get_country(test_id)

        # assert
        assert result_countries.name == expected_country.name

    def test_get_one_no_result(self):
        usecase = CountryUsecases(CountryDBRepo())

        result_countries = usecase.get_country(1)
        assert result_countries is None

    def test_get_one_wrong_params(self):
        usecase = CountryUsecases(CountryDBRepo())

        result_countries = usecase.get_country(-100)
        assert result_countries is None
