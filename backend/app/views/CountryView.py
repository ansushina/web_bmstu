from django.core.exceptions import ObjectDoesNotExist
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.factories.CountryFactory import CountryFactory
from modules.serializers.CountrySerializer import CountrySerializer
from modules.serializers.ErrorSerializer import ErrorSerializer


class CountryView(APIView):
    @swagger_auto_schema(
        operation_summary="Returns info about one country",
        responses={200: CountrySerializer(),
                   404: ErrorSerializer()},
    )
    def get(self, request, pk, format=None):
        usecase = CountryFactory.get_country_usecase()
        try:
            country = usecase.get_country(pk)
            serializer = CountrySerializer(country)
            print(serializer.data)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            raise NotFound
