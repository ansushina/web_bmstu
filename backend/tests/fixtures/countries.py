import pytest

from app.models.Country import CountryORM


@pytest.fixture
def simple_country():
    return CountryORM.objects.create(
        name="россия"
    )


@pytest.fixture
def countries_20():
    countries = [CountryORM.objects.create(name=("country" + str(i))) for i in range(20)]
    return countries


