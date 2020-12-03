from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.factories.CountryFactory import CountryFactory
from modules.serializers.CountrySerializer import CountrySerializer


class CountriesListView(APIView):
    @swagger_auto_schema(
        operation_summary="Returns info about all countries",
        responses={
            200: openapi.Response(
                description="",
                schema=openapi.Schema(type='array',
                                      items=openapi.Schema(
                                          type=openapi.TYPE_OBJECT,
                                          properties={
                                              'name': openapi.Schema(type=openapi.TYPE_STRING),
                                              'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                          }
                                      )
                                      )
            )
        }
    )
    def get(self, request, format=None):
        usecase = CountryFactory.get_country_usecase()

        countries = usecase.get_all_countries()
        ser_countries = []
        for country in countries:
            ser_countries.append(CountrySerializer(country).data)
        # print(serializer.data)
        return Response(ser_countries)
