from rest_framework.views import APIView

from modules.DBRepo.CountryDBRepo import CountryDBRepo
from modules.usecases.CountryUsecases import CountryUsecases
from modules.serializers.CountrySerializer import CountrySerializer
from rest_framework.response import Response


def get_country_usecase() -> CountryUsecases:
    return CountryUsecases(CountryDBRepo())


class CountryView(APIView):
    def get(self, request, pk, format=None):
        usecase = get_country_usecase()
        country = usecase.get_country(pk)
        serializer = CountrySerializer(country)
        print(serializer.data)
        return Response(serializer.data)

