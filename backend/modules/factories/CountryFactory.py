from modules.DBRepo.CountryDBRepo import CountryDBRepo
from modules.usecases.CountryUsecases import CountryUsecases


class CountryFactory:
    @staticmethod
    def get_country_usecase() -> CountryUsecases:
        return CountryUsecases(CountryDBRepo())