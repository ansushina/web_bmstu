from typing import List

from modules.entities.Country import Country
from tests.domain.CountryBuilder import CountryMother


class CountryDBRepoMock:

    @staticmethod
    def get(country_id) -> Country:
        return CountryMother.one().build()

    @staticmethod
    def get_all() -> List[Country]:
        return [CountryMother.one().build(), CountryMother.two().build()]
