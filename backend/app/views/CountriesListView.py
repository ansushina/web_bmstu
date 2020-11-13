from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from modules.DBRepo.CountryDBRepo import CountryDBRepo
from modules.usecases.CountryUsecases import CountryUsecases
from modules.serializers.CountriesListSerializer import CountriesListSerializer
from rest_framework.response import Response


def get_country_usecase() -> CountryUsecases:
    return CountryUsecases(CountryDBRepo())


class CountriesListView(APIView):
    def get(self, request, format=None):
        usecase = get_country_usecase()
        countries = usecase.get_all_countries()
        print(countries)
        countries_serialiser = {
            'countries': countries
        }
        serializer = CountriesListSerializer(countries_serialiser)
        print(serializer.data)
        return Response(serializer.data)
