from django.http import HttpRequest

from app.views.CountriesListView import CountriesListView
from app.views.CountryView import CountryView
from modules.DBRepo.CountryDBRepo import CountryDBRepo
from modules.entities.Country import Country
from tests.domain.CountryBuilder import CountryMother


def countryToDict(country: Country):
    return {
        'name': country.name,
        'id': country.id
    }


class TestCountryView:
    def test_get_mock(self, client, mocker):
        # arrange
        test_country = CountryMother.one().build()
        test_id = 1
        mocker.patch('modules.DBRepo.CountryDBRepo.CountryDBRepo.get', return_value=test_country)
        view = CountryView()

        # act
        resp = view.get(HttpRequest(), test_id)

        # assert
        assert countryToDict(test_country) == resp.data

    def test_all_mock(self, client, mocker):
        # arrange
        test_countries = [CountryMother.one().build(), CountryMother.two().build()]
        mocker.patch('modules.DBRepo.CountryDBRepo.CountryDBRepo.get_all', return_value=test_countries)
        expected_resp = [countryToDict(test_countries[i]) for i in range(len(test_countries))]
        view = CountriesListView()

        # act
        resp = view.get(HttpRequest())

        # assert
        assert expected_resp == resp.data

    # def test_get_country(self, simple_country, client):
    #     # arrange
    #     test_country = CountryDBRepo.decode_orm_country(simple_country)
    #
    #     # act
    #     resp = client.get("/api/v1/countries/" + str(test_country.id) + "/")
    #
    #     # assert
    #     assert countryToDict(test_country) == resp.json()
    #
    # def test_get_all_countries(self, countries_20, client):
    #     # arrange
    #     test_countries = [CountryDBRepo.decode_orm_country(countries_20[i]) for i in range(len(countries_20))]
    #     expected_resp = [countryToDict(test_countries[i]) for i in range(len(test_countries))]
    #
    #     # act
    #     resp = client.get("/api/v1/countries/")
    #
    #     # assert
    #     assert expected_resp == resp.json()
