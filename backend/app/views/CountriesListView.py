from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.factories.CountryFactory import CountryFactory
from modules.serializers.CountriesListSerializer import CountriesListSerializer


class CountriesListView(APIView):
    @swagger_auto_schema(
        operation_summary="Returns info about all countries",
        responses={200: CountriesListSerializer(), }
    )
    def get(self, request, format=None):
        usecase = CountryFactory.get_country_usecase()

        countries = usecase.get_all_countries()
        countries_serializer = {
            'countries': countries
        }

        serializer = CountriesListSerializer(countries_serializer)
        print(serializer.data)
        return Response(serializer.data)
