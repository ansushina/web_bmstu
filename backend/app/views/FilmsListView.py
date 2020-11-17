from django.http import QueryDict
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.factories.FilmFactory import FilmFactory
from modules.serializers.ErrorSerializer import ErrorSerializer
from modules.serializers.FilmQuerySerializer import FilmQuerySerializer
from modules.serializers.FilmsListSerializer import FilmsListSerializer


class FilmsListView(APIView):
    @swagger_auto_schema(
        operation_summary="Returns all films",
        responses={200: FilmsListSerializer(),
                   400: ErrorSerializer()},
        query_serializer=FilmQuerySerializer())
    def get(self, request, format=None):
        usecase = FilmFactory.get_film_usecase()
        query_params = QueryDict(query_string=self.request.GET.urlencode(), mutable=True)
        params = dict(query_params)
        # print(params)
        ser_params = FilmQuerySerializer(data=query_params)
        if not ser_params.is_valid():
            raise ParseError()
        films = usecase.get_all_films(params)
        # print(films)
        films_serialiser = {
            'films': films
        }
        serializer = FilmsListSerializer(films_serialiser)
        # print(serializer.data)
        return Response(serializer.data)
