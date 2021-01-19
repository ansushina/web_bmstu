from pytest_mock import mocker

from modules.DBRepo.CountryDBRepo import CountryDBRepo
from modules.entities.Country import Country
from modules.usecases.CountryUsecases import CountryUsecases
from tests.domain.CountryBuilder import CountryMother
from tests.mocks.CountryDBRepoMock import CountryDBRepoMock


class TestCountriesUsecase:
    def test_get_success(self, mocker):
        # arrange
        expected_countries = [CountryMother.one().build(), CountryMother.two().build()]
        mocker.patch('modules.DBRepo.CountryDBRepo.CountryDBRepo.get_all', return_value=expected_countries)
        usecase = CountryUsecases(CountryDBRepo())

        # act
        result_countries = usecase.get_all_countries()

        # assert
        for i in range(len(expected_countries)):
            assert result_countries[i].name == expected_countries[i].name

    def test_get_one_success_london(self, mocker):
        # arrange
        test_id = 1
        expected_country = CountryMother.one().build()
        mocker.patch('modules.DBRepo.CountryDBRepo.CountryDBRepo.get', return_value=expected_country)
        usecase = CountryUsecases(CountryDBRepo())

        # act
        result_countries = usecase.get_country(test_id)

        # assert
        assert result_countries.name == expected_country.name

    def test_get_one_my_mock(self):
        # arrange
        test_id = 1
        expected_country = CountryMother.one().build()
        usecase = CountryUsecases(CountryDBRepoMock())

        # act
        result_countries = usecase.get_country(test_id)

        # assert
        assert result_countries.name == expected_country.name

    def test_get_all_my_mock(self):
        # arrange
        expected_countries = [CountryMother.one().build(), CountryMother.two().build()]
        usecase = CountryUsecases(CountryDBRepoMock())

        # act
        result_countries = usecase.get_all_countries()

        # assert
        for i in range(len(expected_countries)):
            assert result_countries[i].name == expected_countries[i].name

    # def test_get_one_no_result(self):
    #     usecase = CountryUsecases(CountryDBRepo())
    #
    #     result_countries = usecase.get_country(1)
    #     assert result_countries is None
    #
    # def test_get_one_wrong_params(self):
    #     usecase = CountryUsecases(CountryDBRepo())
    #
    #     result_countries = usecase.get_country(-100)
    #     assert result_countries is None
