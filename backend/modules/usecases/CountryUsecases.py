from typing import List

from modules.entities.Country import Country


class CountryUsecases:
    def __init__(self, country_repo):
        self.country_repo = country_repo

    def get_country(self, country_id) -> Country:
        country = self.country_repo.get(country_id)
        return country

    def get_all_countries(self) -> List[Country]:
        countries = self.country_repo.get_all()
        return countries

