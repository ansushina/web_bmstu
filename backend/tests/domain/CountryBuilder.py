from modules.entities.Country import Country


class CountryMother:
    @staticmethod
    def one():
        country = CountryBuilder()
        country.name = 'country1'
        return country

    @staticmethod
    def two():
        country = CountryBuilder()
        country.name = 'country2'
        return country


class CountryBuilder:
    def __init__(self):
        self.name = ""
        self.id = 0

    def build(self):
        return Country(name=self.name, id=self.id)