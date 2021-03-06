from typing import List

from django.core.exceptions import ObjectDoesNotExist

from app.models.Country import CountryORM
from modules.entities.Country import Country


class CountryDBRepo:
    @staticmethod
    def decode_orm_country(orm_country):
        return Country(id=orm_country.id,
                       name=orm_country.name)

    @staticmethod
    def get(country_id) -> Country:
        try:
            orm_country = CountryORM.objects.get(pk=country_id)
            return CountryDBRepo.decode_orm_country(orm_country)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def get_all() -> List[Country]:
        orm_countries = CountryORM.objects.all()
        countries = []
        for orm_country in orm_countries:
            countries.append(CountryDBRepo.decode_orm_country(orm_country))
        return countries
