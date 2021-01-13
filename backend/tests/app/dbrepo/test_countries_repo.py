from modules.DBRepo.CountryDBRepo import CountryDBRepo


class TestCountriesRepo:
    def test_get_success(self, simple_country):
        # arrange
        expected_country = CountryDBRepo.decode_orm_country(simple_country)
        test_id = simple_country.id

        # act
        result_country = CountryDBRepo.get(country_id=test_id)

        # assert
        assert result_country.name == expected_country.name

    def test_get_fail_noe_found(self):
        # arrange
        test_id = 1

        # act
        result_country = CountryDBRepo.get(country_id=test_id)

        # assert
        assert result_country is None

    def test_get_fail_not_normal(self):
        # arrange
        test_id = 1

        # act
        result_country = CountryDBRepo.get(country_id=test_id)

        # assert
        assert result_country is None

    def test_get_all_success(self, countries_20):
        # arrange
        expected_countries = []
        for g in countries_20:
            expected_countries.append(CountryDBRepo.decode_orm_country(g))

        # act
        result_countries = CountryDBRepo.get_all()

        # assert
        for i in range(len(expected_countries)):
            assert result_countries[i].name == expected_countries[i].name

    def test_get_all_no_results(self):
        # arrange
        expected_countries = []

        # act
        result_countries = CountryDBRepo.get_all()

        # assert
        assert result_countries == expected_countries
